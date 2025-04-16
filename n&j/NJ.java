package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.DcMotorEx;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.util.Range;

@TeleOp(name="Robot:JerNatProject", group="Robot")
public class JerNatProJect extends LinearOpMode {

    public DcMotorEx leftMotor = null;
    public DcMotorEx rightMotor = null;
    public DcMotorEx armMotor = null;

    // Power constants for manual moves (if needed)
    public static final double ARM_UP_POWER   = 0.30;
    public static final double ARM_DOWN_POWER = -0.25;

    // PID constants (tune these experimentally)
    double Kp = 0.02;
    double Ki = 0.001;
    double Kd = 0.005;
    double lastError = 0;
    double integral = 0;

    // Deadband threshold (encoder counts)
    final int DEAD_BAND = 3;

    // Variables for arm target control
    int desiredArmPos = 0;       // Raw desired position based on input
    int smoothedTarget = 0;      // Smoothed target used for PID
    double armSmoothingFactor = 0.2; // Lower factor => smoother (but slower) adjustments

    @Override
    public void runOpMode() {
        // Initialize motors from hardware map
        leftMotor  = hardwareMap.get(DcMotorEx.class, "leftMotor");
        rightMotor = hardwareMap.get(DcMotorEx.class, "rightMotor");
        armMotor   = hardwareMap.get(DcMotorEx.class, "armMotor");

        // Reverse left motor direction if needed for tank drive
        leftMotor.setDirection(DcMotorEx.Direction.REVERSE);
        rightMotor.setDirection(DcMotorEx.Direction.FORWARD);
        armMotor.setDirection(DcMotorEx.Direction.FORWARD);

        // Reset and initialize encoders
        armMotor.setMode(DcMotorEx.RunMode.STOP_AND_RESET_ENCODER);
        leftMotor.setMode(DcMotorEx.RunMode.RUN_USING_ENCODER);
        rightMotor.setMode(DcMotorEx.RunMode.RUN_USING_ENCODER);
        armMotor.setMode(DcMotorEx.RunMode.RUN_USING_ENCODER);

        // Telemetry to indicate robot is ready
        telemetry.addData("Status", "Robot Ready. Press START.");
        telemetry.update();

        waitForStart();

        while (opModeIsActive()) {
            double left = gamepad1.left_stick_y;
            double right = gamepad1.right_stick_y;

            // ----------- Update Desired Arm Position Based on Gamepad ----------- //
            if (gamepad1.dpad_down && desiredArmPos <= 0) {
                desiredArmPos = armMotor.getCurrentPosition() + 30;
            } else if (gamepad1.dpad_up && desiredArmPos >= -330) {
                desiredArmPos = armMotor.getCurrentPosition() - 30;
            } else if (gamepad1.left_bumper && desiredArmPos >= -330) {
                desiredArmPos = -300;
            } else if (gamepad1.right_bumper) {
                // Return to resting position and zero power
                desiredArmPos = 0;
            }
            // Clip desired position within allowed range.
            desiredArmPos = Range.clip(desiredArmPos, -340, 0);
            
            // ----------- Smooth the Target Update ----------- //
            smoothedTarget = (int)lerp(smoothedTarget, desiredArmPos, armSmoothingFactor);

            // ----------- PID Computation ----------- //
            int currentPos = armMotor.getCurrentPosition();
            int error = smoothedTarget - currentPos;
            // Anti-windup: reset integral if error is very small
            if (Math.abs(error) < 5) {
                integral = 0;
            } else {
                integral += error;
            }
            double derivative = error - lastError;
            lastError = error;

            double pidOutput = (Kp * error) + (Ki * integral) + (Kd * derivative);
            
            // Scale down the power when close to target ("slow zone")
            int slowZone = 50;  // adjust as needed
            if (Math.abs(error) < slowZone) {
                double rampFactor = (double)Math.abs(error) / slowZone;
                pidOutput *= rampFactor;
            }
            
            // Enforce deadband near the resting position
            if (Math.abs(smoothedTarget) <= DEAD_BAND && Math.abs(currentPos) <= DEAD_BAND) {
                pidOutput = 0;
            }
            
            // ----------- Set Arm Motor Power ----------- //
            // Using RUN_USING_ENCODER for manual PID control
            armMotor.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
            armMotor.setPower(pidOutput);

            // ----------- Drive the Robot ----------- //
            moveBot(left, right);

            // ----------- Telemetry ----------- //
            telemetry.addData("Current Position", currentPos);
            telemetry.addData("Smoothed Target", smoothedTarget);
            telemetry.addData("Desired Position", desiredArmPos);
            telemetry.addData("Error", error);
            telemetry.addData("PID Output", pidOutput);
            telemetry.addData("Left", "%.2f", left);
            telemetry.addData("Right", "%.2f", right);
            telemetry.update();
        }
    }

    public void moveBot(double lm, double rm) {
        leftMotor.setPower(lm);
        rightMotor.setPower(rm);
    }
    
    public double lerp(double current, double target, double factor) {
        return current + (target - current) * factor;
    }
}

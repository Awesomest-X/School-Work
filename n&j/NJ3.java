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
    int slowZone = 50; // within 50 counts, begin to reduce power
    int desiredArmPos = 0;       // Desired raw position based on input
    int smoothedTarget = 0;      // Smoothed (ramped) target for the arm
    double armSmoothingFactor = 0.2; // Lower factor means slower, smoother changes
            double slowPower = 0.3;

    // Deadband threshold (encoder counts) so the motor isn't powered at or near zero
    final int DEAD_BAND = 3;

    @Override
    public void runOpMode() {
        // Initialize motors from the hardware map
        leftMotor  = hardwareMap.get(DcMotorEx.class, "leftMotor");
        rightMotor = hardwareMap.get(DcMotorEx.class, "rightMotor");
        armMotor   = hardwareMap.get(DcMotorEx.class, "armMotor");

        // Reverse left motor if necessary for tank drive, set others accordingly
        leftMotor.setDirection(DcMotorEx.Direction.REVERSE);
        rightMotor.setDirection(DcMotorEx.Direction.FORWARD);
        armMotor.setDirection(DcMotorEx.Direction.FORWARD);

        // Initialize encoders
        armMotor.setMode(DcMotorEx.RunMode.STOP_AND_RESET_ENCODER);
        leftMotor.setMode(DcMotorEx.RunMode.RUN_USING_ENCODER);
        rightMotor.setMode(DcMotorEx.RunMode.RUN_USING_ENCODER);
                armMotor.setMode(DcMotorEx.RunMode.RUN_USING_ENCODER);

        // Initially, set the arm to RUN_TO_POSITION so it holds a position after moving

        // Telemetry to signal the robot is ready
        telemetry.addData("Status", "Robot Ready. Press START.");
        telemetry.update();

        waitForStart();

        while (opModeIsActive()) {
            double left  = gamepad1.left_stick_y;
            double right = gamepad1.right_stick_y;
            
            // --- Update Desired Arm Position Based on Gamepad ---
            // Use gamepad buttons to increment or decrement the desired arm position
            if (gamepad1.dpad_down && desiredArmPos <= 0) {
                // Lower arm: increase encoder count
                desiredArmPos = armMotor.getCurrentPosition() + 20;
                slowZone = 50;
                 slowPower = 0.3;
            } else if (gamepad1.dpad_up && desiredArmPos >= -340) {
                // Raise arm: decrease encoder count (assuming negative values indicate upward motion)
                desiredArmPos = armMotor.getCurrentPosition() - 20;
                slowZone = 50;
                 slowPower = 0.35;

            } else if (gamepad1.right_bumper) {
                // Return to resting (zero) position
                desiredArmPos = 0;
                 slowZone = 170; // within 170 counts, begin to reduce power
                 slowPower = 0.2;

            }
            // Clip the desired arm position within allowed limits
            desiredArmPos = Range.clip(desiredArmPos, -340, 0);

            // --- Smooth the Target Update using LERP ---
            smoothedTarget = (int) lerp(smoothedTarget, desiredArmPos, armSmoothingFactor);

            // --- Optionally Apply a Slow Zone Near the Target ---
            // This helps the arm decelerate as it nears the setpoint.
            int currentPos = armMotor.getCurrentPosition();
            int error = smoothedTarget - currentPos;
            if (Math.abs(error) < slowZone) {
                slowPower = (double) Math.abs(error) / slowZone;
            }
            
            // Enforce a deadband: if the setpoint is around zero, ensure the motor is not powered unnecessarily.
            if (Math.abs(smoothedTarget) <= DEAD_BAND && Math.abs(currentPos) <= DEAD_BAND) {
                slowPower = 0;
            }

            // --- Set Arm Motor to RUN_TO_POSITION with the Smoothed Target ---
            armMotor.setTargetPosition(smoothedTarget);
                    armMotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);

            // Use the slowPower factor to scale the power provided to the motor’s 1built-in controller
            // This helps the internal PID not to overshoot. You can experiment with a base power value.
            if(desiredArmPos == 0){
                slowPower = Math.max(slowPower, 0.1);
            }
            
            armMotor.setPower(slowPower);

            // --- Drive the Robot as Usual ---
            moveBot(left, right);

            // --- Telemetry for debugging ---
            telemetry.addData("Current Pos", currentPos);
            telemetry.addData("Smoothed Target", smoothedTarget);
            telemetry.addData("Desired Pos", desiredArmPos);
            telemetry.addData("Error", error);
            telemetry.addData("Slow Power", slowPower);
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

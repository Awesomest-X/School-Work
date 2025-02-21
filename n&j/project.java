/* Copyright (c) 2017 FIRST. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted (subject to the limitations in the disclaimer below) provided that
 * the following conditions are met:
 *
 * Redistributions of source code must retain the above copyright notice, this list
 * of conditions and the following disclaimer.
 *
 * Redistributions in binary form must reproduce the above copyright notice, this
 * list of conditions and the following disclaimer in the documentation and/or
 * other materials provided with the distribution.
 *
 * Neither the name of FIRST nor the names of its contributors may be used to endorse or
 * promote products derived from this software without specific prior written permission.
 *
 * NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS
 * LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.DcMotorEx;
import com.qualcomm.robotcore.eventloop.opmode.OpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.util.Range;

/*
 * This OpMode executes a Tank Drive control TeleOp a direct drive robot
 * The code is structured as an Iterative OpMode
 *
 * In this mode, the left and right joysticks control the left and right motors respectively.
 * Pushing a joystick forward will make the attached motor drive forward.
 * It raises and lowers the claw using the Gamepad Y and A buttons respectively.
 * It also opens and closes the claws slowly using the left and right Bumper buttons.
 *
 * Use Android Studio to Copy this Class, and Paste it into your team's code folder with a new name.
 * Remove or comment out the @Disabled line to add this OpMode to the Driver Station OpMode list
 */

@TeleOp(name="Robot: Teleop Tank", group="Robot")

public class JerNatProject extends LinearOpMode {

    /* Declare OpMode members. */
    public DcMotorEx  leftMotor   = null;
    public DcMotorEx  rightMotor  = null;
    public DcMotorEx  armMotor     = null;
 
          // sets rate to move servo
    public static final double ARM_UP_POWER    =  0.30 ;   // Run arm motor up at 30% power
    public static final double ARM_DOWN_POWER  = -0.25 ;   // Run arm motor down at -25% power

    /*                                         
     * Code to run ONCE when the driver hits INIT
     */
    @Override
    public void runOpMode() {
        // Define and Initialize Motors
        leftMotor  = hardwareMap.get(DcMotorEx.class, "leftMotor");
        rightMotor = hardwareMap.get(DcMotorEx.class, "rightMotor");
        armMotor    = hardwareMap.get(DcMotorEx.class, "armMotor");

        // To drive forward, most robots need the motor on one side to be reversed, because the axles point in opposite directions.
        // Pushing the left and right sticks forward MUST make robot go forward. So adjust these two lines based on your first test drive.
        // Note: The settings here assume direct drive on left and right wheels.  Gear Reduction or 90 Deg drives may require direction flips
        leftMotor.setDirection(DcMotorEx.Direction.REVERSE);
        rightMotor.setDirection(DcMotorEx.Direction.FORWARD);
        armMotor.setDirection(DcMotorEx.Direction.FORWARD);

        // If there are encoders connected, switch to RUN_USING_ENCODER mode for greater accuracy
        armMotor.setMode(DcMotorEx.RunMode.STOP_AND_RESET_ENCODER);
           leftMotor.setMode(DcMotorEx.RunMode.RUN_USING_ENCODER);
        rightMotor.setMode(DcMotorEx.RunMode.RUN_USING_ENCODER);
        armMotor.setMode(DcMotorEx.RunMode.RUN_USING_ENCODER);

        // Send telemetry message to signify robot waiting;
        telemetry.addData(">>>>", "Robot Ready.  Press START.");  
        telemetry.update();
        //
      waitForStart();

        while (opModeIsActive()) {
        double left;
        double right;
       int Arm = 0;
        // Run wheels in tank mode (note: The joystick goes negative when pushed forward, so negate it)
        left = gamepad1.left_stick_y;
        right = gamepad1.right_stick_y;

        leftMotor.setPower(left);
        rightMotor.setPower(right);

        // Use gamepad buttons to move the arm up (Y) and down (A)
        if (gamepad1.dpad_down && armMotor.getCurrentPosition() <= 0){
            Arm = Arm + 10;
            power = ARM_UP_POWER;
        }
        else if (gamepad1.dpad_up && armMotor.getCurrentPosition() >= -400){
          Arm = Arm - 10;
            power = ARM_DOWN_POWER;
        }
          else if (armMotor.getCurrentPosition() >= 0){
             power = 0;
        }
        else {
      armMotor.setTargetPosition(Arm); 
          armMotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
            armMotor.setPower(power);
}
        // Send telemetry message to signify robot running;
        telemetry.addData(">>>>Power", armMotor.getPower());    
        telemetry.addData(">>>Position", armMotor.getCurrentPosition());  
        telemetry.addData(">>>Target", armMotor.getTargetPosition());  
        telemetry.addData(">>>Target", Arm);  
        telemetry.addData(">>>>Left",  "%.2f", left);
        telemetry.addData(">>>>Right", "%.2f", right);
        telemetry.update();
    }
}
}

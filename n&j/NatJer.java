package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.DcMotorEx;
import com.qualcomm.robotcore.eventloop.opmode.OpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.util.Range;
import com.qualcomm.robotcore.util.ElapsedTime;


@TeleOp(name="Robot:JerNatProject", group="Robot")

public class JerNatProJect extends LinearOpMode {

    /* Declare OpMode members. */
    public DcMotorEx  leftMotor   = null;
    public DcMotorEx  rightMotor  = null;
    public DcMotorEx  armMotor     = null;
    private ElapsedTime     runtime = new ElapsedTime();          // sets rate to move servo
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
       double power = 0;
       boolean cool = false;
       int Arm = 0;
int currentArmTarget = 0;
double armSmoothingFactor = 0.2; // Lower = smoother

        // To drive forward, most robots need the motor on one side to be reversed, 
        // because the axles point in opposite directions.
        // Pushing the left and right sticks forward MUST make robot go forward.
        // So adjust these two lines based on your first test drive.
        // Note: The settings here assume direct drive on left and right wheels. 
        // Gear Reduction or 90 Deg drives may require direction flips
        leftMotor.setDirection(DcMotorEx.Direction.REVERSE);
        rightMotor.setDirection(DcMotorEx.Direction.FORWARD);
        armMotor.setDirection(DcMotorEx.Direction.FORWARD);

        // Because of the encoders connected, switch to RUN_USING_ENCODER mode for greater accuracy
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

      
        // Run wheels in tank mode (note: The joystick goes negative when pushed forward, so negate it)
        left = gamepad1.left_stick_y;
        right = gamepad1.right_stick_y;


        // Use gamepad buttons to move the arm up (Y) and down (A)
        if (gamepad1.dpad_down && Arm <= 0){
            Arm = armMotor.getCurrentPosition() + 30;
            power = ARM_UP_POWER;
        }
        else if (gamepad1.dpad_up && Arm >= -330){
          Arm = armMotor.getCurrentPosition() - 30;
            power = ARM_DOWN_POWER;
        }
         else if (gamepad1.left_bumper && Arm >= -330){
          Arm = -300;
            power = ARM_DOWN_POWER;
        }
        else if (gamepad1.right_bumper ){
             Arm = 0;
        }
        else if (gamepad1.right_bumper){
             power = 0;
        }
        
                        Arm = Range.clip(Arm, -340, 0);
                        currentArmTarget = (int) lerp(currentArmTarget, Arm, armSmoothingFactor);
      armMotor.setTargetPosition(currentArmTarget); 
          armMotor.setMode(DcMotor.RunMode.RUN_TO_POSITION);
            armMotor.setPower(power);

/*if (gamepad1.a){
    runtime.reset();
    cool = true;
}
 else if (gamepad1.b){
    cool = false;
}

if (cool = true && runtime.seconds() < 3.5) {
     moveBot(1,-1);
   }
   else {*/
    moveBot(left,right);
//}




 // Send telemetry message to signify robot running;
        telemetry.addData(">>>Power", armMotor.getPower());    
        telemetry.addData(">>>Position", armMotor.getCurrentPosition());  
        telemetry.addData(">>>Target", armMotor.getTargetPosition());  
        telemetry.addData(">>>Left",  "%.2f", left);
        telemetry.addData(">>>Right", "%.2f", right);
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

// Linear interpolation between current and target based on factor

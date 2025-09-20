# t-gauge-automation

This repository contains program(s) to autonomously control a T-gauge railway using a Raspberry Pi. As other model gauges make use of automation, this project aims to do the same for T-gauge.

## Usage

### Required parts

- [Raspberry Pi](https://thepihut.com/collections/raspberry-pi?gad_source=1&gad_campaignid=18204675107&gbraid=0AAAAADfQ4GE75prXEQM2_mF5ZhG2M1GJ9&gclid=CjwKCAjwobnGBhBNEiwAu2mpFJVjj7zbKeBvpw9hozwNw3gvgL_GSsjFlGhJ8TVXqcMKW4j8R1ogURoCdI4QAvD_BwE) & SD card
- [DVR8833](https://www.adafruit.com/product/3297?srsltid=AfmBOoqVCeQRaqIkwqthE3CqrfcR0SvQXWTcdEyBI5o4lsspDOR-eEg8) - Needed to drive PWM at 4.5V
- T-gauge [trainset](https://www.tgauge.com/product/434/class-67-starter-set-with-hand-held-controller/687e1762a3967878ecd210388b21be15) starter pack

### Setup Rasberry Pi and T-gauge trainset

1. Connect Pi and circuitry
2. Clone the repo:\
   `clone <repo-url`
3. Navigate to the head of directory to run this script (creates and installs the virtual enviroment and dependencies):\
   `source ./scripts/create_venv.sh`
4. Circuit diagram for T-gauge operation:

- **1st Note**: The Fritzing [diagram](./Documentation/t-gauge-automation-schematic.fzz) stored on repository
- **2nd Note**: T-Gauge operates at **4.5V**, whereas the Pi can only deliver **3.3V**. The DV8833 is used to bring the output voltage to ~4.45V. This ensures the smooth operation of the locomotive
  <img width="1646" height="864" alt="image" src="https://github.com/user-attachments/assets/053eef1b-0013-4102-b718-087b06b0587d" />

### Run T-gauge locomotive

5. Once complete, the program can be run:\
   `python ./main_app/main_app.py`

- Note: The Pi uses PWM at **137Hz** with varying duty cycle to control the locomotive. This frequency has been derived from scoping the controller unit that comes with the trainset.

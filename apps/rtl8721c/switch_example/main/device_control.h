/* ***************************************************************************
 *
 * Copyright 2019 Samsung Electronics All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
 * either express or implied. See the License for the specific
 * language governing permissions and limitations under the License.
 *
 ****************************************************************************/
#include <stdbool.h>
#include <string.h>
#include "st_dev.h"
#include "PinNames.h"
#include <gpio_api.h>
#include "gpio_irq_api.h"
#include "gpio_irq_ex_api.h"


#define GPIO_OUTPUT_COLORLED_0			PB_4
#define GPIO_OUTPUT_NOTIFICATION_LED	PA_26
#define GPIO_INPUT_BUTTON				PB_1
#define GPIO_BUTTON_0					PB_2

#define GPIO_OUTPUT_MAINLED		PB_5

enum notification_led_gpio_state {
	NOTIFICATION_LED_GPIO_ON = 0,
	NOTIFICATION_LED_GPIO_OFF = 1,
};

enum main_led_gpio_state {
	MAINLED_GPIO_ON = 1,
	MAINLED_GPIO_OFF = 0,
};

enum led_animation_mode_list {
	LED_ANIMATION_MODE_IDLE = 0,
	LED_ANIMATION_MODE_FAST,
	LED_ANIMATION_MODE_SLOW,
};

enum button_gpio_state {
	BUTTON_GPIO_RELEASED = 1,
	BUTTON_GPIO_PRESSED = 0,
};

#define BUTTON_DEBOUNCE_TIME_MS 20
#define BUTTON_LONG_THRESHOLD_MS 5000
#define BUTTON_DELAY_MS 300

enum button_event_type {
	BUTTON_LONG_PRESS = 0,
	BUTTON_SHORT_PRESS = 1,
};

void button_isr_handler(void *arg);
int get_button_event(int* button_event_type, int* button_event_count);
void led_blink(int gpio, int delay, int count);
void change_led_state(int noti_led_mode);
void hardware_gpio_init(void);

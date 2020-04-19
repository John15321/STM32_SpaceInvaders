################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include Drivers/STM32F1xx_HAL_Driver/Src/subdir.mk
-include Core/Startup/subdir.mk
-include Core/Src/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
NUCLEO-F103RB-UART-JOYSTICK.elf \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
NUCLEO-F103RB-UART-JOYSTICK.list \

OBJCOPY_BIN += \
NUCLEO-F103RB-UART-JOYSTICK.bin \


# All Target
all: NUCLEO-F103RB-UART-JOYSTICK.elf secondary-outputs

# Tool invocations
NUCLEO-F103RB-UART-JOYSTICK.elf: $(OBJS) $(USER_OBJS) E:\Uczelnia\Semestr\ 4\PTM\L\Project\STM32_SpaceInvaders\NUCLEO-F103RB-UART-JOYSTICK\NUCLEO-F103RB-UART-JOYSTICK\STM32F103RBTX_FLASH.ld
	arm-none-eabi-gcc -o "NUCLEO-F103RB-UART-JOYSTICK.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m3 -T"E:\Uczelnia\Semestr 4\PTM\L\Project\STM32_SpaceInvaders\NUCLEO-F103RB-UART-JOYSTICK\NUCLEO-F103RB-UART-JOYSTICK\STM32F103RBTX_FLASH.ld" --specs=nosys.specs -Wl,-Map="NUCLEO-F103RB-UART-JOYSTICK.map" -Wl,--gc-sections -static --specs=nano.specs -mfloat-abi=soft -mthumb -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

NUCLEO-F103RB-UART-JOYSTICK.list: $(EXECUTABLES)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "NUCLEO-F103RB-UART-JOYSTICK.list"
	@echo 'Finished building: $@'
	@echo ' '

NUCLEO-F103RB-UART-JOYSTICK.bin: $(EXECUTABLES)
	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "NUCLEO-F103RB-UART-JOYSTICK.bin"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) *
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_BIN)

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets

let micro_temp = 0
input.onButtonPressed(Button.A, function () {
    micro_temp = input.temperature()
    basic.showNumber(micro_temp)
    basic.pause(1000)
    basic.clearScreen()
})

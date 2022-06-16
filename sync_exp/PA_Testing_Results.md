The table below shows testing results for different power amplifications of transmitter and receiver NRF24L01 modules. The transmitted packets are 100. A one "1" in the table indicates that the power mode is used.
Note that the NRF24L01 modules are locates close to each other, and the transmitter sends one packet for each 0.5 seconds.

|   Trial No.   |                 Transmitter                                   |         Receiver                   | Packets Received |
|:-------:|:------:|:------:|:-----------:|:------:|:--------:|:------:|:------:|:--------:|:------:|:--------:|:------------:|
| ------- | PA_MIN | PA_LOW |   PA_HIGH   | PA_MAX | PA_ERROR | PA_MIN | PA_LOW |  PA_HIGH | PA_MAX | PA_ERROR | ------------ |
|       1       |    1   |    0   |      0      |    0   |     0    |    1   |    0   |     0    |    0   |     0    |        97        |
|       2       |    0   |    1   |      0      |    0   |     0    |    1   |    0   |     0    |    0   |     0    |        98        |
|       3       |    0   |    0   |      1      |    0   |     0    |    1   |    0   |     0    |    0   |     0    |        100       |
|       4       |    0   |    0   |      0      |    1   |     0    |    1   |    0   |     0    |    0   |     0    |        100       |
|       5       |    0   |    0   |      0      |    0   |     1    |    1   |    0   |     0    |    0   |     0    |        100       |

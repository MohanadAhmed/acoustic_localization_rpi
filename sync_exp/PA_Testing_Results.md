The table below shows testing results for different power amplifications of transmitter and receiver NRF24L01 modules. The transmitted packets are 100. A one "1" in the table indicates that the power mode is used.
Note that the NRF24L01 modules are locates close to each other, and the transmitter sends one packet for each 0.1 seconds.

|   Trial No.   |        |        | Transmitter |        |          |        |        | Receiver |        |          | Packets Received |
|:-------:|:------:|:------:|:-----------:|:------:|:--------:|:------:|:------:|:--------:|:------:|:--------:|:------------:|
| ------- | PA_MIN | PA_LOW |   PA_HIGH   | PA_MAX | PA_ERROR | PA_MIN | PA_LOW |  PA_HIGH | PA_MAX | PA_ERROR | ------------ |
|       1       |    1   |    0   |      0      |    0   |     0    |    1   |    0   |     0    |    0   |     0    |        97 - 99 - 97 - 99  - 100 - 99       | 
|       2       |    0   |    1   |      0      |    0   |     0    |    1   |    0   |     0    |    0   |     0    |        93 - 90 - 81 - 51  - 100 - 55       |
|       3       |    0   |    0   |      1      |    0   |     0    |    1   |    0   |     0    |    0   |     0    |        99 - 98 - 97 - 100 - 100 - 100      |
|       4       |    0   |    0   |      0      |    1   |     0    |    1   |    0   |     0    |    0   |     0    |        95 - 99 - 96 - 97  - 100 - 95       |
|       5       |    0   |    0   |      0      |    0   |     1    |    1   |    0   |     0    |    0   |     0    |        96 - 98 - 93 - 99  - 98  - 97       |


The table below shows testing results for different power amplifications of transmitter and receiver NRF24L01 modules. The transmitted packets are 500. A one "1" in the table indicates that the power mode is used.
Note that the NRF24L01 modules are locates close to each other, and the transmitter sends one packet for each 0.1 seconds.

|   Trial No.   |        |        | Transmitter |        |          |        |        | Receiver |        |          | Packets Received |
|:-------:|:------:|:------:|:-----------:|:------:|:--------:|:------:|:------:|:--------:|:------:|:--------:|:------------:|
| ------- | PA_MIN | PA_LOW |   PA_HIGH   | PA_MAX | PA_ERROR | PA_MIN | PA_LOW |  PA_HIGH | PA_MAX | PA_ERROR | ------------ |
|       1       |    1   |    0   |      0      |    0   |     0    |    1   |    0   |     0    |    0   |     0    |        497 - 498 - 497       |
|       2       |    0   |    1   |      0      |    0   |     0    |    1   |    0   |     0    |    0   |     0    |        497 - 499 - 499       |
|       3       |    0   |    0   |      1      |    0   |     0    |    1   |    0   |     0    |    0   |     0    |        500 - 498 - 498       |
|       4       |    0   |    0   |      0      |    1   |     0    |    1   |    0   |     0    |    0   |     0    |        495 - 496 - 494       |
|       5       |    0   |    0   |      0      |    0   |     1    |    1   |    0   |     0    |    0   |     0    |        493 - 499 - 493       |

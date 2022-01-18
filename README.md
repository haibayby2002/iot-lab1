#This is lab1 project from HCMUT
###Student name: Nguyen Quy Hai
###Stu_id: 2052974

###Some explanation
- In `updatePosition`, I update the <b>longitude</b> and <b>latitude</b> based on the current one and 
make some small variable each 10 seconds. Because one can not make a large distance
from the previous 10 seconds, I set the range for change is from -0.0001 to 0.0001 which
means that for each 10 seconds, the <b>latitude</b> and <b>longitude</b> can
increase or decrease at maximum 0.0001 degree. Moreover, the boundary of the 
position will be used to limit them only in acceptable value!
- I also use this way of thinking for <b>temperature</b> and <b>humid</b>, but in
these cases, I apply only in integer. Therefore, I use `randrange` for <b>temperature</b> and <b>humid</b>
but use `uniform` for the <b>latitude</b> and <b>longitude</b>
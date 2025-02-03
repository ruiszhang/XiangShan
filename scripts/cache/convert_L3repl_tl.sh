sed 's/|/ /g' | awk --bignum '

func chnstr(chn) {
  split("A B C D E", channels, " ");
  return channels[chn + 1]
}

func opstr(chn, op) {

  a_op[1] = "PutFullData"
	a_op[2] = "PutPartialData"
	a_op[3] = "ArithmeticData"
	a_op[4] = "LogicalData"
	a_op[5] = "Get"
	a_op[6] = "Hint"
	a_op[7] = "AcquireBlock"
	a_op[8] = "AcquirePerm"

  b_op[1] = "PutFullData"
  b_op[2] = "PutPartialData"
  b_op[3] = "ArithmeticData"
  b_op[4] = "LogicalData"
  b_op[5] = "Get"
  b_op[6] = "Hint"
  b_op[7] = "Probe"

  c_op[1] = "AccessAck"
  c_op[2] = "AccessAckData"
  c_op[3] = "HintAck"
  c_op[4] = "Invalid Opcode"
  c_op[5] = "ProbeAck"
  c_op[6] = "ProbeAckData"
  c_op[7] = "Release"
  c_op[8] = "ReleaseData"

  d_op[1] = "AccessAck"
  d_op[2] = "AccessAckData"
  d_op[3] = "HintAck"
  d_op[4] = "Invalid Opcode"
  d_op[5] = "Grant"
  d_op[6] = "GrantData"
  d_op[7] = "ReleaseAck"

  ret = "Unknown OP"
  switch(chn) {
    case 0:
      ret = a_op[op+1]
      break;
    case 1:
      ret = b_op[op+1]
      break;
    case 2:
      ret = c_op[op+1]
      break;
    case 3:
      ret = d_op[op+1]
      break;
    case 4:
      ret = "GrantAck"
      break;
  }
  return ret
}

func paramstr(chn, param) {

  split("Grow NtoB_Grow NtoT_Grow BtoT", grow, "_")
	split("Cap toT_Cap toB_Cap toN", cap, "_")
	split("Shrink TtoB_Shrink TtoN_Shrink BtoN_Report TotT_Report BtoB_Report NtoN", report, "_")

  ret = "Reserved"
  switch(chn){
    case 0:
      ret = grow[param+1]
      break;
    case 1:
      ret = cap[param+1]
      break;
    case 2:
      ret = report[param+1]
      break;
    case 3:
      ret = cap[param+1]
      break;
  }
  return ret
}

func hitwaystr(hitvec1, hitvec2, hitvec3, hitvec4) {
  split("0 1 2 3 miss", hitway, " ");
  ret = "Reserved"

  if(hitvec1 ==1 && hitvec2 ==0 && hitvec3 ==0 && hitvec4 ==0){
    ret = hitway[1];
  }
  else if(hitvec1 ==0 && hitvec2 ==1 && hitvec3 ==0 && hitvec4 ==0) {
    ret = hitway[2];
  }
  else if(hitvec1 ==0 && hitvec2 ==0 && hitvec3 ==1 && hitvec4 ==0) {
    ret = hitway[3];
  }
  else if(hitvec1 ==0 && hitvec2 ==0 && hitvec3 ==0 && hitvec4 ==1) {
    ret = hitway[4];
  }
  else if(hitvec1 ==0 && hitvec2 ==0 && hitvec3 ==0 && hitvec4 ==0) {
    ret = hitway[5];
  }
  else {
    ret = "Wrong";
  }
  return ret
}

func agevecstr(age1, age2, age3, age4) {
  ageVec = $((age1 + age2 + age3 + age4));
  return ageVec
}

func addrstr(tag, set) {
  offset = 000000;
  addr = $((tag + set + offset));
  return addr
}



{
  wayCnt0 = $2;
  wayCnt1 = $3;
  wayCnt2 = $4;
  wayCnt3 = $5;
  age0 = $6;
  age1 = $7;
  age2 = $8;
  age3 = $9;
  hitWay = $10;
  hit = $11;
  selectedWay = $12;
  useCount = $13;
  tripCount = $14;
  slice = $15;
  set = $16;
  tag = $17;
  param = $18;
  opcode = $19;
  channel = $20;
  stamp = $21;
  site = $22;




  $1 = stamp;                             # timestamp
  $2 = chnstr(channel);                    # channel
  $3 = opstr(channel, opcode);             # opcode
  $4 = paramstr(channel, param);          # param                              
  $5 = sprintf("tag=%lx", tag);
  $6 = sprintf("set=%lx", set);
  $7 = sprintf("selectedWay=%d", selectedWay);
  $8 = sprintf("hit=%d", hit); 
  $9 = sprintf("hitWay=%s", hitWay); 
  $10 = sprintf("agevec=%d%d%d%d", age0, age1, age2, age3);
  $11 = sprintf("wayCnt0=%ld", wayCnt0)
  $12 = sprintf("wayCnt1=%ld", wayCnt1)
  $13 = sprintf("wayCnt2=%ld", wayCnt2)
  $14 = sprintf("wayCnt3=%ld", wayCnt3)
  $15 = sprintf("tripCount=%d", tripCount)
  $16 = sprintf("useCount=%d", useCount)           
  $17 = sprintf("sliceId=%d", bank)
  $18 = "";
  $19 = "";
  $20 = "";
  $21 = "";
  $22 = "";
  $23 = "";
  $24 = "";
  $NF = "";   # remove log id
}

1                                   # print every line
'

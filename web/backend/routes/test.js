/*#Zizhao Li (1267416) zizhaol2@student.unimelb.edu.au (Suzhou, China)
#Fu Zhu (1166186) fuzhu@student.unimelb.edu.au (Melbourne, Australia)
#Chuting Wang (1074511) chutingw@student.unimelb.edu.au (Xi’an, China)
#Xuezhu Wu (938808) xuezhuw@student.unimelb.edu.au (Hangzhou, China)
#Yuepeng Sheng (1048382) yuepengs@student.unimelb.edu.au (Shanghai, China)
*/

const express = require("express");
const router = express.Router();

ip = "http://admin:password@172.26.130.194:5984/";

const nano = require("nano")(ip);

router.get("/", async function (req, res, next) {
  var health = "hello database"
  res.send(health);
});

module.exports = router;

/*#Zizhao Li (1267416) zizhaol2@student.unimelb.edu.au (Suzhou, China)
#Fu Zhu (1166186) fuzhu@student.unimelb.edu.au (Melbourne, Australia)
#Chuting Wang (1074511) chutingw@student.unimelb.edu.au (Xi’an, China)
#Xuezhu Wu (938808) xuezhuw@student.unimelb.edu.au (Hangzhou, China)
#Yuepeng Sheng (1048382) yuepengs@student.unimelb.edu.au (Shanghai, China)
*/

var express = require('express');
var router = express.Router();
const nano = require('nano')('http://admin:password@172.26.130.194:5984');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/graph', function(req, res){
    res.redirect('/');
});

router.get("/test_0", function (req, res, next) {
  const alice = nano.use('alice')
  const info = "error";
  try {
   info = alice.insert({ happy: true }, 'rabbits')
  }catch (e) {
  // failed
  console.error(e)
	}
res.send(info);
});

router.get("/test_db", async function (req, res, next) {
  var data = [];
  var db = nano.use("realtime_mapreduce");
  await db.list({ include_docs: true }).then((body) => {
    body.rows.forEach((doc) => {
      doc = doc.doc;
      data.push(doc);
    });
  });
  res.send(data);
});





module.exports = router;

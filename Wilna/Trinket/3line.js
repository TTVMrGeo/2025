const fs = require('node:fs');
var LineX, LineY, LineZ

fs.readFile('results.txt', 'utf8', (err, data) => {
  data = data.split("\r\n")
  for (let i = 0; i < data.length; i++) {
    LineZ = LineY
    LineY = LineX
    LineX = data[i]
  }
  console.log(LineZ)
  console.log(LineY)
  console.log(LineX)
});
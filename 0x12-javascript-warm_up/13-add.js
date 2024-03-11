#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);

#!/usr/bin/node
exports.add = function (x, m) {
  return x + m;
};
// It computes the sum of two integers.

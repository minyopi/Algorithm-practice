/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  if (s.length % 2 != 0) return false;

  const str = { "{": "}", "[": "]", "(": ")" };
  s = s.split("");

  const arr = [];
  for (let i = 0; i < s.length; i++) {
    if (str[s[i]]) {
      arr.push(str[s[i]]);
      continue;
    }

    if (s[i] == arr.at(-1)) arr.pop();
    else return false;
  }

  return arr.length == 0 ? true : false;
};

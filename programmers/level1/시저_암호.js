const isLowerCaseAndExceed = item > 44 && item < 91 && item + n > 90;
const isUpperCaseAndExceed = item > 96 && item < 123 && item + n > 122;
const isSpace = item === 32;

function solution(s, n) {
  const answer = s
    .split("")
    .map((item) => item.charCodeAt(0))
    .map((item) => {
      if (isSpace) return 32;
      if (isLowerCaseAndExceed || isUpperCaseAndExceed) return item + n - 26;

      return item + n;
    })
    .map((item) => String.fromCharCode(item))
    .join("");

  return answer;
}

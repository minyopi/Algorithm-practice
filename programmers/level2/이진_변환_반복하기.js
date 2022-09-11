function solution(s) {
  const answer = [0, 0];
  while (s !== "1") {
    const temp = s
      .split("")
      .filter((item) => item !== "0")
      .join("");
    answer[1] += s.length - temp.length;

    s = temp.length.toString(2);
    answer[0] += 1;
  }
  return answer;
}

//  s = s.replace(/0/g, "");
// 를 활용해서 0을 삭제하는 방법도 있다.

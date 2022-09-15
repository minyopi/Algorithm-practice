function solution(n) {
  const countN = [...n.toString(2).match(/1/g)].length;
  while (true) {
    n++;
    if (countN === [...n.toString(2).match(/1/g)].length) return n;
  }
}

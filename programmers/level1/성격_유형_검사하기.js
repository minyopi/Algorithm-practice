function solution(survey, choices) {
  const MBTI = {};
  const types = ["RT", "CF", "JM", "AN"];

  types.forEach((type) => type.split("").forEach((char) => (MBTI[char] = 0)));

  survey.forEach(
    (type, idx) =>
      (MBTI[choices[idx] < 4 ? type[0] : type[1]] += Math.abs(choices[idx] - 4))
  );

  return types
    .map((type) => (MBTI[type[0]] < MBTI[type[1]] ? type[1] : type[0]))
    .join("");
}

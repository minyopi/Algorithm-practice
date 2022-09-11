function solution(id_list, report, k) {
  const set_report = new Set(report);
  const userList = id_list.map((item) => {
    return { name: item, report: [], reported: 0 };
  });

  [...set_report]
    .map((item) => item.split(" "))
    .forEach((reportItem) => {
      userList.forEach((user) => {
        if (user.name == reportItem[0]) user.report.push(reportItem[1]);
        if (user.name == reportItem[1]) user.reported++;
      });
    });

  const blockedUsers = userList
    .filter((user) => user.reported >= k)
    .map((user) => user.name);

  const answer = userList.map((user) => {
    return blockedUsers.filter((blockedUser) =>
      user.report.includes(blockedUser)
    ).length;
  });

  return answer;
}

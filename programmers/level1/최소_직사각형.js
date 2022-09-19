function solution(sizes) {
  let width = 0,
    height = 0;

  sizes
    .map((size) => {
      if (size[0] < size[1]) return [size[1], size[0]];
      return size;
    })
    .forEach((size) => {
      if (size[0] > width) width = size[0];
      if (size[1] > height) height = size[1];
    });

  return width * height;
}

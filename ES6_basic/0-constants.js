export function taskFirst() {
  const task = 'I prefer const when I can.\n';
  return task;
}

export function getLast() {
  return ' is okay\n';
}

export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
}

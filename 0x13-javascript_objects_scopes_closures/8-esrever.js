#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  list.map(
    (ele) => {
      rev.unshift(ele);
      return 0;
    }
  );
  return rev;
};

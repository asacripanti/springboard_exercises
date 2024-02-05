/** product: calculate the product of an array of numbers. */

function product(nums, idx = 0) {
  if (idx === nums.length) return 1;
  return nums[idx] * product(nums, idx + 1);
}

/** longest: return the length of the longest word in an array of words. */

function longest(words, idx = 0, maxLength = 0) {
  // Base case: if the index is equal to the length of the array, return the maxLength
  if (idx === words.length) {
    return maxLength;
  } else {
    // Recursive case: compare the length of the current word with the maxLength
    const currentLength = words[idx].length;
    const newMaxLength = Math.max(maxLength, currentLength);

    // Recursive call for the next word (incrementing the index)
    return longest(words, idx + 1, newMaxLength);
  }
}

/** everyOther: return a string with every other letter. */

function everyOther(str, idx = 0, result = '') {
  if (idx >= str.length) {
    return result;
  } else {
    // Recursive case: append every other character to the result
    result += str[idx];

    // Recursive call for the next character (skip one character)
    return everyOther(str, idx + 2, result);
  }
}

/** isPalindrome: checks whether a string is a palindrome or not. */

function isPalindrome(str, idx = 0) {
  let leftIdx = idx;
  let rightIdx = str.length - idx - 1;
  if (leftIdx >= rightIdx) return true;
  if (str[leftIdx] !== str[rightIdx]) return false;
  return isPalindrome(str, idx + 1);
}

/** findIndex: return the index of val in arr (or -1 if val is not present). */

function findIndex(arr, val, idx = 0) {
  if (idx >= arr.length) {
    return -1;
  } else {
    // Recursive case: compare the current element with the target
    if (arr[idx] === val) {
      // If the current element matches the target, return the current index
      return idx;
    } else {
      // If not, make a recursive call for the next index
      return findIndex(arr, val, idx + 1);
    }
  }
}

/** revString: return a copy of a string, but in reverse. */

function revString(str, idx = 0, newStr = "") {
  if (newStr.length === str.length) return newStr;
  newStr += str[str.length - 1 - idx];
  return revString(str, idx + 1, newStr);
}

/** gatherStrings: given an object, return an array of all of the string values. */

function gatherStrings(obj) {
  let result = [];

  for (let key in obj) {
    if (typeof obj[key] === 'string') {
      // If the current value is a string, add it to the result array
      result.push(obj[key]);
    } else if (typeof obj[key] === 'object' && !Array.isArray(obj[key])) {
      // If the current value is an object (excluding arrays), make a recursive call
      result = result.concat(gatherStrings(obj[key]));
    }
    // Ignore arrays, as they are not expected in the example
  }

  return result;
}

/** binarySearch: given a sorted array of numbers, and a value,
 * return the index of that value (or -1 if val is not present). */

function binarySearch(arr, val) {

}

module.exports = {
  product,
  longest,
  everyOther,
  isPalindrome,
  findIndex,
  revString,
  gatherStrings,
  binarySearch
};

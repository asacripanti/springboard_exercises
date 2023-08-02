function findFloor() {
    let low = 0;
    let high = arr.length - 1;
    
    return findFloorHelper(arr, num, low, high);
  }
  
  function findFloorHelper(arr, num, low, high) {
    if (low > high) return -1;
    if (num >= arr[high]) return arr[high];
  
    let mid = Math.floor((low + high) / 2);
  
    if (arr[mid] === num) return arr[mid];
  
    if (mid > 0 && arr[mid - 1] <= num && num < arr[mid]) {
      return arr[mid - 1];
    }
  
    if (num < arr[mid]) {
      return findFloorHelper(arr, num, low, mid - 1);
    }
  
    return findFloorHelper(arr, num, mid + 1, high);
}

module.exports = findFloor
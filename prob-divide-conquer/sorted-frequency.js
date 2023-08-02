function sortedFrequency(arr, val) {
    let firstCount = findFirstCount(arr, val);
    if(firstCount === -1){
        return -1;
    }

    let lastCount = findLastCount(arr, val);

    return lastCount - firstCount + 1;

}

function findFirstCount(arr, val, low = 0, high = arr.length - 1) {
    if (high >= low) {
      let mid = low + Math.floor((high - low) / 2);
  
      if ((mid === 0 || arr[mid - 1] < val) && arr[mid] === val) {
        return mid;
      } else if (arr[mid] < val) {
        return findFirstOccurrence(arr, val, mid + 1, high);
      }
      return findFirstOccurrence(arr, val, low, mid - 1);
    }
    return -1;
  }
  
  function findLastCount(arr, val, low = 0, high = arr.length - 1) {
    if (high >= low) {
      let mid = low + Math.floor((high - low) / 2);
  
      if ((mid === arr.length - 1 || arr[mid + 1] > val) && arr[mid] === val) {
        return mid;
      } else if (arr[mid] > val) {
        return findLastOccurrence(arr, val, low, mid - 1);
      }
      return findLastOccurrence(arr, val, mid + 1, high);
    }
    return -1;
  }

module.exports = sortedFrequency
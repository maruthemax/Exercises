function sortedFrequency(arr, num) {
    const firstIndex = findFirst(arr, num);
    if (firstIndex === -1) return -1;
    const lastIndex = findLast(arr, num);
    return lastIndex - firstIndex + 1;
}

function findFirst(arr, num) {
    let left = 0;
    let right = arr.length - 1;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (arr[mid] === num) {
            if (mid === 0 || arr[mid - 1] < num) return mid;
            right = mid - 1;
        } else if (arr[mid] < num) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

function findLast(arr, num) {
    let left = 0;
    let right = arr.length - 1;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (arr[mid] === num) {
            if (mid === arr.length - 1 || arr[mid + 1] > num) return mid;
            left = mid + 1;
        } else if (arr[mid] < num) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

module.exports = sortedFrequency
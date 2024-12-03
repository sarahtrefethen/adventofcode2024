use std::fs;

fn test_safety (sequence:&str) -> bool {
    let mut nums = sequence.split(" ").map(|n| n.parse::<i32>().expect("entries should all be numbers")); 
    let mut previous = nums.next().expect("there should be a first number");
    let mut is_first = true;
    let mut is_ascending = true;
    for num in nums {
        let diff = num - previous;
        if (diff == 0) || (diff.abs() > 3) {
            return false;
        } else if is_first {
            is_ascending = diff > 0;
        } else if is_ascending && (diff < 0) {
            return false;
        } else if !is_ascending && (diff > 0) {
            return false;
        } 
    
        is_first = false;
        previous = num;
    }
    true
}

pub(crate) fn day02 () {
    let path = "input/D02.txt";
    let contents = fs::read_to_string(path).expect("file should open");
    let mut total = 0;
    for line in contents.lines() {
        if test_safety(line) {
            total += 1;
        }
    }
    println!("Part 1: {}", total)
}
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

fn test_dampened_safety(sequence:&str) -> bool {
    if test_safety(sequence) {
        return true;
    } 
    let mut nums:Vec<i32> = sequence.split(" ").map(|n| n.parse::<i32>().expect("entries should all be numbers")).collect(); 

    for i in 0..nums.len() {
        let mut copy = nums.clone();
        copy.remove(i);
        let removed_sequence = copy.into_iter().map(|x| x.to_string()).collect::<Vec<String>>().join(" ");
        if test_safety(&removed_sequence) {
            return true;
        };
    };
    false
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
    println!("Part 1: {}", total);

    total = 0;
    for line in contents.lines() {
        if test_dampened_safety(line) {
            total += 1;
        }
    }
    println!("Part 2: {}", total)

}
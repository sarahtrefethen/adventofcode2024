use std::fs;

pub(crate) fn day01 () {
    let path = "input/D01.txt";
    let contents = fs::read_to_string(path).expect("file should open");
    let mut left_column: Vec<i32> = vec![];
    let mut right_column: Vec<i32> = vec![];
    for line in contents.lines() {
        let nums: Vec<&str> = line.split_ascii_whitespace().collect();

        let first: i32 = nums.first().expect("asdf").parse().expect("input should be a number");
        let next: i32 = nums.last().expect("asdf").parse().expect("input should be a number");
        left_column.push(first);
        right_column.push(next);
    }

    left_column.sort();
    right_column.sort();

    let mut right_iter = right_column.iter();

    let diffs: Vec<i32> = left_column.iter().map(|x| (x-right_iter.next().unwrap()).abs()).collect();

    println!("Part 1: {:?}", diffs.iter().sum::<i32>());

}
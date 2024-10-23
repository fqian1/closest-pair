fn merge(left: &mut Vec<(f32, f32)>, right: &mut Vec<(f32, f32)>) {
    let mut combined = Vec::new();
    let mut i = 0;
    let mut j = 0;

    while i < left.len() && j < right.len() {
        if left[i] <= right[j] {
            combined.push(left[i]);
            i += 1;
        } else {
            combined.push(right[j]);
            j += 1;
        }
    }

    while i < left.len() {
        combined.push(left[i]);
        i += 1;
    }

    while j < right.len() {
        combined.push(right[j]);
        j += 1;
    }

    left.clear();
    right.clear();

    let mid = combined.len() / 2;
    left.extend_from_slice(&combined[..mid]);
    right.extend_from_slice(&combined[mid..]);
}

fn merge_sort(points: &mut Vec<(f32, f32)>) -> &mut Vec<(f32, f32)> {
    if points.len() <= 1 {
        return points;
    }
    let mid = points.len() / 2;
    let (left, right) = points.split_at_mut(mid);
    merge(merge_sort(left), merge_sort(right));
    points
}

// fn merge_sort(points: &mut Vec<(f32, f32)>) {
//     if points.len() <= 1 {
//         return points;
//     }
// }

fn main() {
    let points = String::from(
        "(-1.0, 6.0)
(-7.0, 0.0)
(-3.0, -6.0)
(3.0, -5.0)
(7.0, -7.0)
(-4.0, 3.0)
(-6.0, 2.0)
(-8.0, -3.0)",
    );

    let mut points_vec: Vec<(f32, f32)> = Vec::new();
    for line in points.lines() {
        let line = line.trim_matches(|x| x == '(' || x == ')');
        let mut coords = line.split(",");
        let x = coords.next().unwrap().trim().parse::<f32>().unwrap();
        let y = coords.next().unwrap().trim().parse::<f32>().unwrap();
        points_vec.push((x, y));
    }
    println!("{:?}", points_vec);
}

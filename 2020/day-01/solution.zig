const std = @import("std");
const fs = std.fs;
const io = std.io;

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    var file = try fs.cwd().openFile("input", .{});
    defer file.close();

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer {
        _ = gpa.deinit();
    }

    var bufReader = io.bufferedReader(file.reader()).reader();
    var buf: [512]u8 = undefined;

    var map = std.AutoArrayHashMap(u32, bool).init(&gpa.allocator);
    defer map.deinit();
    var map2 = std.AutoArrayHashMap(u32, u32).init(&gpa.allocator);
    defer map2.deinit();

    while (try bufReader.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        const num = try std.fmt.parseUnsigned(u32, line, 10);
        try map.put(num, true);
        try map2.put(2020 - num, num);
    }

    var mapIter = map.iterator();
    var map2Iter = map2.iterator();
    while (mapIter.next()) |e| {
        const first = e.key_ptr.*;
        map2Iter.reset();

        while (map2Iter.next()) |e2| {
            const twoSummed = e2.key_ptr.*;
            const third = e2.value_ptr.*;
            const second = if (twoSummed >= first) twoSummed - first else 0;
            if (map.getEntry(second)) |e3| {
                try stdout.print("Found three: {d} - {d} - {d}: {d}\n", .{ first, second, third, first * second * third });
            }
        }

        // Solution 1
        const key = 2020 - first;
        if (map.getEntry(key)) |e2| {
            try stdout.print("Found two keys: {d} and {d}: {d}\n", .{ key, e2.key_ptr.*, key * e2.key_ptr.* });
        }
    }
}

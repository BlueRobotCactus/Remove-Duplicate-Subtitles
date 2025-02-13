def read_srt_blocks(filename):
    """
    Reads an SRT file and returns a list of blocks.
    Each block is stored as a list of lines (including the index and time).
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    blocks = []
    current_block = []

    for line in lines:
        # Blocks are separated by a blank line.
        if line.strip() == "" and current_block:
            blocks.append(current_block)
            current_block = []
        else:
            current_block.append(line)

    # If there's no trailing blank line, catch the last block
    if current_block:
        blocks.append(current_block)

    return blocks


def blocks_are_identical(block1, block2):
    """
    Returns True if two blocks are identical (ignoring their block number lines).
    This ignores the first line of each block, because that line is the old index
    which we will reassign anyway. If you want to compare absolutely everything,
    remove the [1:] slicing.
    """
    # Strip the old index line and compare the rest.
    return block1[1:] == block2[1:]


def deduplicate_srt_blocks(blocks):
    """
    Returns a list of blocks with consecutive duplicate blocks removed.
    """
    deduped = []
    for i, block in enumerate(blocks):
        if i == 0:
            deduped.append(block)
        else:
            if not blocks_are_identical(block, deduped[-1]):
                deduped.append(block)
    return deduped


def write_srt(filename, blocks):
    """
    Writes the list of blocks to an SRT file with correct sequential numbering.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for i, block in enumerate(blocks, start=1):
            # Replace the old block number with the new one
            # (the first line of each block is the old index, so we overwrite it).
            new_block = [str(i)] + block[1:]
            for line in new_block:
                f.write(line + "\n")
            f.write("\n")  # blank line after each block


def main():
    input_file = "input.srt"
    output_file = "output.srt"

    # 1. Read blocks
    blocks = read_srt_blocks(input_file)

    # 2. Deduplicate
    deduped = deduplicate_srt_blocks(blocks)

    # 3. Write new SRT
    write_srt(output_file, deduped)

    print(f"Done! Wrote deduplicated subtitles to {output_file}")


if __name__ == "__main__":
    main()

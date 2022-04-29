import test_sudoku

def print_msg(fun):
    print('Testing of the', fun, 'function has been successfully completed!')

if __name__ == "__main__":
    test = test_sudoku.SudokuTestCase()
    test.test_group()
    print_msg('group()')
    test.test_get_row()
    print_msg('get_row()')
    test.test_get_col()
    print_msg('get_col()')
    test.test_get_block()
    print_msg('get_block()')
    test.test_find_empty_positions()
    print_msg('find_empty_positions()')
    test.test_find_possible_values()
    print_msg('find_possible_values()')
    test.test_check_solution()
    print_msg('check_solution()')
    test.test_generate_sudoku()
    print_msg('generate_sudoku()')
    test.test_solve()
    print_msg('solve()')

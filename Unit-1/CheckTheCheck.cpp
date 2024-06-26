
// Unit = 1
// Program Name = Check The Check

// Name  = Varun Kotgire
// class = TYCSE-A
// Roll  = 79
// Batch = 4

#include <vector>
#include <iostream>
#include <string>

using namespace std;

bool handleStraight(const vector<string> &board, int x, int y, char target1, char target2)
{
    if ((x - 1 >= 0 && (board[y][x - 1] == target1 || board[y][x - 1] == target2)) ||
        (x + 1 < 8 && (board[y][x + 1] == target1 || board[y][x + 1] == target2)) ||
        (y - 1 >= 0 && (board[y - 1][x] == target1 || board[y - 1][x] == target2)) ||
        (y + 1 < 8 && (board[y + 1][x] == target1 || board[y + 1][x] == target2)))
        return true;

    for (int xc = -1; xc + x - 1 >= 0 && board[y][xc + x] == '.'; --xc)
        if (board[y][xc + x - 1] == target1 || board[y][xc + x - 1] == target2)
            return true;

    for (int xc = 1; xc + x + 1 < 8 && board[y][xc + x] == '.'; ++xc)
        if (board[y][xc + x + 1] == target1 || board[y][xc + x + 1] == target2)
            return true;

    for (int yc = -1; yc + y - 1 >= 0 && board[y + yc][x] == '.'; --yc)
        if (board[y + yc - 1][x] == target1 || board[y + yc - 1][x] == target2)
            return true;

    for (int yc = 1; yc + y + 1 < 8 && board[y + yc][x] == '.'; ++yc)
        if (board[y + yc + 1][x] == target1 || board[y + yc + 1][x] == target2)
            return true;

    return false;
}

bool handleDiagonal(const vector<string> &board, int x, int y, char target1, char target2)
{
    bool upLeft(true), upRight(true), downLeft(true), downRight(true);

    for (int c(1); upLeft || upRight || downLeft || downRight; ++c)
    {
        if (upLeft)
        {
            if (x - c >= 0 && y - c >= 0)
            {
                if (board[y - c][x - c] == target1 || board[y - c][x - c] == target2)
                    return true;
                else if (board[y - c][x - c] != '.')
                    upLeft = false;
            }
            else
            {
                upLeft = false;
            }
        }

        if (upRight)
        {
            if (x + c < 8 && y - c >= 0)
            {
                if (board[y - c][x + c] == target1 || board[y - c][x + c] == target2)
                    return true;
                else if (board[y - c][x + c] != '.')
                    upRight = false;
            }
            else
            {
                upRight = false;
            }
        }

        if (downLeft)
        {
            if (x - c >= 0 && y + c < 8)
            {
                if (board[y + c][x - c] == target1 || board[y + c][x - c] == target2)
                    return true;
                else if (board[y + c][x - c] != '.')
                    downLeft = false;
            }
            else
            {
                downLeft = false;
            }
        }

        if (downRight)
        {
            if (x + c < 8 && y + c < 8)
            {
                if (board[y + c][x + c] == target1 || board[y + c][x + c] == target2)
                    return true;
                else if (board[y + c][x + c] != '.')
                    downRight = false;
            }
            else
            {
                downRight = false;
            }
        }
    }

    return false;
}

bool handleKnight(const vector<string> &board, int x, int y, char target)
{
    int knightMoves[8][2] = {{-2, -1}, {-2, 1}, {2, -1}, {2, 1}, {-1, -2}, {1, -2}, {-1, 2}, {1, 2}};
    for (int i = 0; i < 8; ++i)
    {
        int newX = x + knightMoves[i][0];
        int newY = y + knightMoves[i][1];
        if (newX >= 0 && newX < 8 && newY >= 0 && newY < 8 && board[newY][newX] == target)
        {
            return true;
        }
    }
    return false;
}

bool handlePawn(const vector<string> &board, int x, int y, char target, int yChange)
{
    if (y + yChange < 8 && y + yChange >= 0)
    {
        if (x - 1 >= 0 && board[y + yChange][x - 1] == target)
            return true;
        if (x + 1 < 8 && board[y + yChange][x + 1] == target)
            return true;
    }
    return false;
}

int main()
{
    bool forever = true;
    int whitePosx, blackPosx, whitePosy, blackPosy, temp;
    vector<string> board(8);

    for (int t = 1; forever; ++t)
    {
        whitePosx = blackPosx = -1;
        for (int i = 0; i < 8; ++i)
        {
            cin >> board[i];
            temp = board[i].find('k');
            if (temp != string::npos)
            {
                blackPosy = i;
                blackPosx = temp;
            }
            temp = board[i].find('K');
            if (temp != string::npos)
            {
                whitePosy = i;
                whitePosx = temp;
            }
        }

        if (whitePosx == -1)
            break;

        cout << "Game #" << t << ": ";

        if (handlePawn(board, whitePosx, whitePosy, 'p', -1))
            cout << "white king is in check.\n";
        else if (handlePawn(board, blackPosx, blackPosy, 'P', 1))
            cout << "black king is in check.\n";
        else if (handleKnight(board, whitePosx, whitePosy, 'n'))
            cout << "white king is in check.\n";
        else if (handleKnight(board, blackPosx, blackPosy, 'N'))
            cout << "black king is in check.\n";
        else if (handleStraight(board, whitePosx, whitePosy, 'r', 'q'))
            cout << "white king is in check.\n";
        else if (handleStraight(board, blackPosx, blackPosy, 'R', 'Q'))
            cout << "black king is in check.\n";
        else if (handleDiagonal(board, whitePosx, whitePosy, 'b', 'q'))
            cout << "white king is in check.\n";
        else if (handleDiagonal(board, blackPosx, blackPosy, 'B', 'Q'))
            cout << "black king is in check.\n";
        else
            cout << "no king is in check.\n";
    }
}

// Sample Input

// ..k.....
// ppp.pppp
// ........
// .R...B..
// ........
// ........
// PPPPPPPP
// K.......
// rnbqkbnr
// pppppppp
// ........
// ........
// ........
// ........
// PPPPPPPP
// RNBQKBNR
// rnbqk.nr
// ppp..ppp
// ....p...
// ...p....
// .bPP....
// .....N..
// PP..PPPP
// RNBQKB.R
// ........
// ........
// ........
// ........
// ........
// ........
// ........
// ........

// Sample Output

// Game #1: black king is in check.
// Game #2: no king is in check.
// Game #3: white king is in check.

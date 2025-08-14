#include<stdio.h>
#include<stdlib.h>
#include<windows.h> // For Sleep function on Windows

void display(char **g){
    printf("+---+---+---+\n");
    for(int i=0;i<3;i++){
        printf("|");
        for(int j=0;j<3;j++){
            printf(" %c |",g[i][j]);
        }
        printf("\n+---+---+---+\n");
    }
}
void input(char player,char **g){
    int row, col;
    while(1){
        printf("Player %c, enter your move (row and column): ", player);
        scanf("%d %d", &row, &col);
        row--; // Adjust for 0-based index
        col--; // Adjust for 0-based index
        if(row < 0 || row >= 3 || col < 0 || col >= 3 || g[row][col] != ' '){
            printf("Invalid move. Try again.\n");
            continue;
        }
        break;
    }
    g[row][col] = player;
    display(g);
}
    char check_winner(char **g){
        // Check rows
    for(int i=0;i<3;i++){
        if(g[i][0] == g[i][1] && g[i][1] == g[i][2] && g[i][0] != ' ')
            return g[i][0];
    }
    // Check columns
    for(int j=0;j<3;j++){
        if(g[0][j] == g[1][j] && g[1][j] == g[2][j] && g[0][j] != ' ')
            return g[0][j];
    }
    // Check diagonals
    if(g[0][0] == g[1][1] && g[1][1] == g[2][2] && g[0][0] != ' ')
        return g[0][0];
    if(g[0][2] == g[1][1] && g[1][1] == g[2][0] && g[0][2] != ' ')
        return g[0][2];
    
    if(g[0][0] != ' ' && g[0][1] != ' ' && g[0][2] != ' ' &&
       g[1][0] != ' ' && g[1][1] != ' ' && g[1][2] != ' ' &&
       g[2][0] != ' ' && g[2][1] != ' ' && g[2][2] != ' ')
        return 'd'; // Draw
    return ' '; // No winner
}
int minimax(char **g, int depth, int isMaximizing) {
    char winner = check_winner(g);
    if(winner == 'X') return -10 + depth; // Prefer faster wins/losses
    if(winner == 'O') return 10 - depth;
    if(winner == 'd') return 0;
    if(isMaximizing) {
        int bestScore = -1000;
        for(int i=0;i<3;i++) {
            for(int j=0;j<3;j++) {
                if(g[i][j] == ' ') {
                    g[i][j] = 'O';
                    int score = minimax(g, depth + 1, 0);
                    g[i][j] = ' ';
                    if(score > bestScore) bestScore = score;
                }
            }
        }
        return bestScore;
    } else {
        int bestScore = 1000;
        for(int i=0;i<3;i++) {
            for(int j=0;j<3;j++) {
                if(g[i][j] == ' ') {
                    g[i][j] = 'X';
                    int score = minimax(g, depth + 1, 1);
                    g[i][j] = ' ';
                    if(score < bestScore) bestScore = score;
                }
            }
        }
        return bestScore;
    }
}
void ai(char **g){
    int bestScore = -1000;
    int moveRow = -1, moveCol = -1;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(g[i][j] == ' '){
                g[i][j] = 'O';
                int score = minimax(g, 0, 0);
                g[i][j] = ' ';
                if(score > bestScore){
                    bestScore = score;
                    moveRow = i;
                    moveCol = j;
                }
            }
        }
    }
    if(moveRow != -1 && moveCol != -1){
        g[moveRow][moveCol] = 'O';
        display(g);
    } else {
        printf("AI could not find a valid move.\n");
    }
}
int main(){
    // Initialize the game board
    char **g=malloc(3*sizeof(char*));
    for(int i=0;i<3;i++){
        g[i]=malloc(3*sizeof(char));
        for(int j=0;j<3;j++){
            g[i][j]=' ';
        }
    }
    printf("Welcome to Tic-Tac-Toe!\n");
    printf("enter number of players (1 or 2): ");
    int num_players;
    scanf("%d", &num_players);
    if(num_players < 1 || num_players > 2){ 
        printf("Invalid number of players. Exiting.\n");
        for(int i=0;i<3;i++){
            free(g[i]);
        }
        free(g);
        return 1;
    }
    display(g);
    while(1){
        input('X',g);
        char winner = check_winner(g);
        if(winner == 'X' || winner == 'O'){
            printf("Player %c wins!\n", winner);
            break;
        }
        else if(winner == 'd'){
            printf("It's a draw!\n");
            break;
        }
        if(num_players == 1){ 
            printf("AI's turn:\n");
            ai(g);
        }
        else input('O',g);
        winner = check_winner(g);
        if(winner == 'X' || winner == 'O'){
            printf("Player %c wins!\n", winner);
            break;
        }
        else if(winner == 'd'){
            printf("It's a draw!\n");
            break;
        }
    }
    printf("Game over!\n");
    Sleep(2000); // Optional delay for better visibility of the final board
    for(int i=0;i<3;i++){
        free(g[i]);
    }
    free(g);
    return 0;
}
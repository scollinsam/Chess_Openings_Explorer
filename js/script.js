//(Math.abs(orig-dest)%9 == 0 || Math.abs(orig-dest)%7 == 0)

var plib = {1:'rook_black', 2:'knight_black', 3:'bishop_black', 4:'queen_black', 5:'king_black', 6:'bishop_black', 7:'knight_black', 8:'rook_black', 9:'pawn_black', 10:'pawn_black', 11:'pawn_black', 12:'pawn_black', 13:'pawn_black', 14:'pawn_black', 15:'pawn_black', 16:'pawn_black', 17: 'empty', 18: 'empty', 19: 'empty', 20: 'empty', 21: 'empty', 22: 'empty', 23: 'empty', 24: 'empty', 25: 'empty', 26: 'empty', 27: 'empty', 28: 'empty', 29: 'empty', 30: 'empty', 31: 'empty', 32: 'empty', 33: 'empty', 34: 'empty', 35: 'empty', 36: 'empty', 37: 'empty', 38: 'empty', 39: 'empty', 40: 'empty', 41: 'empty', 42: 'empty', 43: 'empty', 44: 'empty', 45: 'empty', 46: 'empty', 47: 'empty', 48: 'empty',49: 'pawn_white', 50: 'pawn_white', 51: 'pawn_white', 52: 'pawn_white', 53: 'pawn_white', 54: 'pawn_white', 55: 'pawn_white', 56: 'pawn_white', 57: 'rook_white', 58: 'knight_white', 59: 'bishop_white', 60: 'queen_white', 61: 'king_white', 62: 'bishop_white', 63: 'knight_white', 64: 'rook_white'}

function printList(){
    for (i=1; i<65; i++){
    console.log(plib[i])
    }
}

var piece_list = {
    bishop: {
        move_set: function(orig, dest){
            if (plib[dest] == 'empty' || plib[dest].split('_')[1] != plib[orig].split('_')[1]){
                var y_orig = Math.floor((orig - 1) / 8)
                var x_orig = orig - (8 * y_orig) - 1
                var y_dest = Math.floor((dest - 1) / 8)
                var x_dest = dest - (8 * y_dest) - 1
                if (Math.abs(y_orig-y_dest) == Math.abs(x_orig - x_dest)){
                    var y_direction = (y_dest-y_orig) / Math.abs(y_dest-y_orig)
                    var x_direction = (x_dest-x_orig) / Math.abs(x_dest-x_orig)
                    for (counter = 1; counter < Math.abs(y_dest-y_orig); counter ++){
                        if (plib[(y_dest * 8 + x_dest + 1) + (8 * counter * y_direction*-1) + (counter * x_direction * -1)] != "empty"){
                            return false
                        }
                    }
                    return true
                } else {
                    return false
                }
            }
        }
    },
    pawn: {
        move_set: function(orig, dest){
            if (plib[dest] == 'empty' || plib[dest].split('_')[1] != plib[orig].split('_')[1]){
                if (plib[orig] == "pawn_black"){
                    if (dest - orig == 8){
                        return true
                    }else if (orig < 17 && orig > 8){
                        if (dest-orig == 16){
                            if (plib[dest-8] == 'empty'){
                                return true
                            }else{
                                return false
                            }

                        }else if (plib[dest].split('_')[1] != plib[orig].split('_')[1]){
                            if (dest - orig == 7 || dest - orig == 9){
                                return true
                            }
                        }
                    }else if (plib[dest].split('_')[1] != plib[orig].split('_')[1]){
                        if (dest - orig == 7 || dest - orig == 9){
                            return true
                        }
                    }
                }else{
                    if (orig - dest == 8){
                        return true
                    }else if (orig < 57 && orig > 48){
                        if (orig - dest == 16){
                            if (plib[parseInt(dest)+8] == 'empty'){
                                return true
                            }else{
                                return false
                            }
                        }else if (plib[dest].split('_')[1] != plib[orig].split('_')[1]){
                            if (dest - orig == -7 || dest - orig == -9){
                                return true
                            }
                        }
                    }else if (plib[dest].split('_')[1] != plib[orig].split('_')[1]){
                        if (dest - orig == -7 || dest - orig == -9){
                            return true
                        }
                    }
                }
            }
        }
    },
    king: {
        move_set: function(orig, dest){
            if (plib[dest] == 'empty' || plib[dest].split('_')[1] != plib[orig].split('_')[1]){
                var y_orig = Math.floor((orig - 1) / 8)
                var x_orig = orig - (8 * y_orig) - 1
                var y_dest = Math.floor((dest - 1) / 8)
                var x_dest = dest - (8 * y_dest) - 1
                if (Math.abs(y_orig-y_dest) < 2 && Math.abs(x_orig-x_dest) < 2){
                    return true
                }else{
                    return false
                }
            }else{
                return false
            }

        }
    },
    knight: {
        move_set: function(orig, dest){
            if (plib[dest] == 'empty' || plib[dest].split('_')[1] != plib[orig].split('_')[1]){
                var y_orig = Math.floor((orig - 1) / 8)
                var x_orig = orig - (8 * y_orig) - 1
                var y_dest = Math.floor((dest - 1) / 8)
                var x_dest = dest - (8 * y_dest) - 1
                if (Math.abs(y_orig-y_dest) + Math.abs(x_orig-x_dest) == 3 && Math.abs(Math.abs(y_orig-y_dest) - Math.abs(x_orig-x_dest)) == 1){
                    return true
                }else{
                    return false
                }
            }else{
                return false
            }
        }
    },
    rook: {
        move_set: function(orig, dest){
            if (plib[dest] == 'empty' || plib[dest].split('_')[1] != plib[orig].split('_')[1]){
                var direction = 0
                var y_orig = Math.floor((orig - 1) / 8)
                var x_orig = orig - (8 * y_orig) - 1
                var y_dest = Math.floor((dest - 1) / 8)
                var x_dest = dest - (8 * y_dest) - 1
                if (y_dest - y_orig == 0 || x_dest - x_orig == 0){
                    if ((dest-orig) % 8 == 0){
                        direction = 8;
                    }else{
                        direction = 1
                    }
                    if (dest-orig < 0){
                        direction = direction * -1
                    }
                    for (counter = 1; counter < ((dest-orig) / direction); counter ++){
                        if (plib[dest - (direction * counter)] != "empty"){
                            return false
                        }
                    }
                    return true
                }else{
                    return false
                }
            }else{
                return false
            }
        }
    },
    queen:{
        move_set: function(orig, dest){
            if (plib[dest] == 'empty' || plib[dest].split('_')[1] != plib[orig].split('_')[1]){
                var y_orig = Math.floor((orig - 1) / 8)
                var x_orig = orig - (8 * y_orig) - 1
                var y_dest = Math.floor((dest - 1) / 8)
                var x_dest = dest - (8 * y_dest) - 1
                if (Math.abs(y_orig-y_dest) == Math.abs(x_orig - x_dest)){
                    var y_direction = (y_dest-y_orig) / Math.abs(y_dest-y_orig)
                    var x_direction = (x_dest-x_orig) / Math.abs(x_dest-x_orig)
                    for (counter = 1; counter < Math.abs(y_dest-y_orig); counter ++){
                        if (plib[(y_dest * 8 + x_dest + 1) + (8 * counter * y_direction*-1) + (counter * x_direction * -1)] != "empty"){
                            return false
                        }
                    }
                    return true
                }else if (y_dest - y_orig == 0 || x_dest - x_orig == 0){
                    if ((dest-orig) % 8 == 0){
                        direction = 8;
                    }else{
                        direction = 1
                    }
                    if (dest-orig < 0){
                        direction = direction * -1
                    }
                    for (counter = 1; counter < ((dest-orig) / direction); counter ++){
                        if (plib[dest - (direction * counter)] != "empty"){
                            return false
                        }
                    }
                    return true
                }else{
                    return false
                }
            }
        }
    }
}







var turn = 'white'
function changeTurn(){
    var turn_message = document.getElementById("turn")
    if (turn_message.innerHTML == "White's turn"){
    turn_message.innerHTML = "Black's turn";
    turn = 'black'}
    else {turn_message.innerHTML = "White's turn"
    turn = 'white'}
}

var board = document.getElementById("chess_board");
for (row_count = 0; row_count < 8; row_count ++){
    var row = document.createElement("tr");
    board.appendChild(row);
    for (square_count = 0; square_count < 8; square_count ++){
        var square_num = row_count*8 + square_count + 1
        var square = document.createElement("td");
        square.setAttribute("id", square_num);
        if ((square_count + row_count) % 2 == 0){
            square.classList.add("white_square")
        }
        else{
            square.classList.add("black_square");
        }
        if (plib[square_num] != "empty") {
            square.classList.add(plib[square_num])
        }

        else {
            square.classList.add("empty")
        }

        row.appendChild(square);

    }
}
var save_orig = 1
var orig_taken_piece = 1
var orig_moved_piece = 1
var save_new = 1
var save_piece = plib[1]
var save_taken_piece = 'queen-white'
var graveyard = []


// changePiece(12, 20, plib[12])
// changePiece(53, 37, plib[52])
function changePiece(prev_pos, new_pos, piece){
    orig_moved_piece = plib[prev_pos]
    orig_taken_piece = plib[new_pos]
    console.log(prev_pos, new_pos, piece)
    var prev = document.getElementById(prev_pos);
    var dest = document.getElementById(new_pos);
    //console.log(style)
    dest.classList.add(piece);
    prev.classList.remove(piece);
    dest.classList.remove(plib[new_pos])
    plib[new_pos] = piece
    plib[prev_pos] = 'empty'
    changeTurn();
    save_orig = prev_pos;
    save_new = new_pos;
    save_piece = piece
    if (move_count >= 4) {
        save()
        getOpening()
    }
}

function undoTurn(){
    const retain = document.getElementById(save_new);
    const returned_piece = document.getElementById(save_orig)
    retain.classList.remove(retain.classList[1])
    retain.classList.add(orig_taken_piece);
    returned_piece.classList.add(orig_moved_piece)
    plib[save_orig] = orig_moved_piece;
    plib[save_new] = orig_taken_piece;
    changeTurn()


}



square_selected = 0

function clicked(loc){
    if (square_selected != 0){
        if (square_selected != loc){
            console.log(((plib[square_selected]).split('_', 1))[0])
            if (piece_list[((plib[square_selected]).split('_', 1))[0]].move_set(square_selected, loc) == true){
                changePiece(square_selected, loc, plib[square_selected])
                }
            square_selected = 0 }
    }
    else if (plib[loc] != "empty"){
        if (plib[loc].split('_')[1]==turn){

        square_selected = loc
        }
    }
    }






board.addEventListener('click', function (e) {
    square = event.target
    clicked(square.id)
})


function save() {
    $.ajax({
        type: 'POST',
        url: '/save',
        contentType: "application/json",
        data: JSON.stringify({
            board: plib
        }),
        success: () => { console.log("board saved successfully")},
        error: () => { console.log("error saving board successfully")}
    });
}

function getOpening() {
    $.ajax({
        type: "GET",
        url: '/getopening',
        dataType: "json",
        success: (data) => {
            console.log(data)
        },
        error: () => {
            console.log('did not receive plib')
        }
    })
}

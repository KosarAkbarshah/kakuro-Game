import { useState, useEffect } from "react";
import "./Board.css";

const Board = () => {
  // state variables
  const [board, setBoard] = useState(null);
  const [editingCell, setEditingCell] = useState(null);

  const updateCellValue = (row, col, value) => {
    // Validate input: must be a number between 1 and 9
    if (!value || isNaN(value) || value < 1 || value > 9) return;

    // Create a new updated board by mapping over rows and columns
    const updatedBoard = board.map((r, rIdx) => {
      return r.map((cell, cIdx) => {
        // Update only the selected cell if it's a number
        if (rIdx === row && cIdx === col && cell.type === "number") {
          return { ...cell, value: parseInt(value, 10) };
        }
        return cell;
      });
    });
    
    setBoard(updatedBoard);
    setEditingCell(null);
  };

  //runs only once on page refresh (F5)
  useEffect(() => {
    const initializeBoard = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        setBoard(data.board); // set the board STATE
      } catch (error) {
        console.error("Error initializing board:", error);
      }
    };

    initializeBoard();
    console.log("re-initialized board")
  }, []);

  const validateBoard = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/validate/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ board }), // Send the current board state
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const data = await response.json();
      alert(data.is_valid ? "Congratulations! You solved the puzzle" : "Sorry, board is not solved, please look again.");
    } catch (error) {
      console.error("Error validating board:", error);
      alert("Error validating board!");
    }
  };

  // Show loading message until board data is available
  if (!board) return <p>Loading board...</p>;

  return (
    <div className="board">
      <table>
        <tbody>
          {board.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((cell, colIndex) => {
                // Check if this cell is currently being edited
                const isEditing = editingCell?.row === rowIndex && editingCell?.col === colIndex;
                
                // Handle cell click to enable editing
                const handleClick = () => {
                  if (cell.type === "number") {
                    setEditingCell({ row: rowIndex, col: colIndex });
                  }
                };
    
                return (
                  <td
                    key={colIndex}
                    className={`cell ${cell.type}`}
                    onClick={handleClick}
                  >
                    {/* Render sum-type cells with sum hints */}
                    {cell.type === "sum" && (
                      <div className="sum-cell">
                        {cell.right_sum !== null && `→${cell.right_sum}`}
                        <br />
                        {cell.down_sum !== null && `↓${cell.down_sum}`}
                      </div>
                    )}
                    
                    {/* Render number cells with editable input */}
                    {cell.type === "number" && (
                      <div className="number-cell">
                        {isEditing ? (
                          <input
                            type="number"
                            min="1"
                            max="9"
                            autoFocus
                            style={{ appearance: "textfield" }}
                            onBlur={(e) => updateCellValue(rowIndex, colIndex, e.target.value)}
                            onKeyDown={(e) => {
                              if (e.key === "Enter") {
                                updateCellValue(rowIndex, colIndex, e.target.value);
                              }
                            }}
                          />
                        ) : (
                          <span>{cell.value}</span>
                        )}
                      </div>
                    )}
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
      <button onClick={validateBoard} className="btn">Check Answer</button>
    </div>

  );
};

export default Board;
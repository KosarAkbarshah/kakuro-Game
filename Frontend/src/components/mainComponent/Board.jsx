import { useState, useEffect } from "react";
import "./Board.css"

const Board = () => {
  const [board, setBoard] = useState(null);

  useEffect(() => {
    async function fetchBoard() {
      try {
        const response = await fetch("http://127.0.0.1:8000/");
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        setBoard(data.board);
      } catch (error) {
        console.error("Error fetching board:", error);
      }
    }
    fetchBoard();
  }, []);

  if (!board) return <p>Loading board...</p>;

  return (
    <div className="board">
      <table>
        <tbody>
          {board.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((cell, colIndex) => (
                <td
                  key={colIndex}
                  className={`cell ${cell.type}`}
                >
                  {cell.type === "sum" && (
                    <div className="sum-cell">
                      {cell.right_sum !== null && `→${cell.right_sum}`}
                      <br />
                      {cell.down_sum !== null && `↓${cell.down_sum}`}
                    </div>
                  )}
                  {cell.type === "number" && (
                    <div className="number-cell">
                      {cell.value}
                    </div>
                  )}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Board;


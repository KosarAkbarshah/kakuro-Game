import React from 'react'
import './Main.css'
import { assets } from '../../assets/assets'

const main = () => {
    return (
        <>
            <main>
                <div className='header'>
                    <h1>Welcome to Kakuro Game</h1>
                </div>
                <div className='gameplay'>

                    <div className='instructions'>
                        <h2>How to play?</h2>
                        <p>
                            Kakuro is a fun and simple number puzzle game! Your goal is to fill the empty boxes in the grid with numbers from 1 to 9 so that the sums match the clues provided. Each clue represents the total you need to achieve in its corresponding row or column. The trick is that numbers in a row or column can’t repeat, so you need to think carefully about how to distribute them. Use logic and deduction to figure out the right numbers, and have fun solving the puzzle!
                        </p>
                    </div>

                    <div className="box">
                        <div className='cubes'>

                            {/* <!-- Row 1 --> */}
                            <div class="cell black"></div>
                            <div class="cell black"></div>
                            <div class="cell black hint">4\</div>
                            <div class="cell white"></div>

                            {/* <!-- Row 2 --> */}
                            <div class="cell black"></div>
                            <div class="cell black hint">4\</div>
                            <div class="cell white"></div>
                            <div class="cell white"></div>

                            {/* <!-- Row 3 --> */}
                            <div class="cell black hint">6\</div>
                            <div class="cell white"></div>
                            <div class="cell white"></div>
                            <div class="cell black"></div>
                        </div>
                    </div>
                    <img src={assets.bg1} alt="" />
                </div>
            </main>
        </>
    )
}

export default main;

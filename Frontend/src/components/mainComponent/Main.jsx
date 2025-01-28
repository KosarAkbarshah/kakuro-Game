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
                        <div className="form">
                            <label className='label'>Username</label>
                            <input type="text" className="input" placeholder="Enter your username" />
                            <label className='label'>Email</label>
                            <input type="email" className="input" placeholder="Enter your email" />
                            <label className='label'>Password</label>
                            <input type="password" className="input" placeholder="Enter your password" />
                        </div>
                        <span className='guest'>Don't have an account? Continue as Guest</span>
                        <button className='guestbtn'>Guest Login</button>
                    </div>
                    <img src={assets.bg1} alt="" />
                </div>
            </main>
        </>
    )
}

export default main;

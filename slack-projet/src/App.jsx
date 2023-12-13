import * as React from "react";
import styled from "styled-components"
import SideBar from "./components/SideBar";

import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";
import './App.css'
import Header from "./components/Header";

function App() {

  return (
    <div className="app">
        <Router>
            <>
          <Header />
            <AppBody>
              <SideBar />
                <Routes>

                    <Route path="/"   exact />
                    {/* chat */}
                </Routes>
                </AppBody>
            </>
        </Router>

    </div>
  )
}

export default App;

const AppBody = styled.div`
    display: flex;
    height: 100vh;

`
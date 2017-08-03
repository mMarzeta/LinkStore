import React, {Component} from 'react';
import axios from 'axios';
import './App.css';


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            receivedData: "",
        }
    }

    componentWillMount() {
        axios({
            method: 'get',
            responseType: 'json',
            url: 'http://127.0.0.1:8000/link-store/',

        })
            .then(response => {
                this.setState({
                    receivedData: response.data,
                });
                console.log("data: " + response + "status: " + response.status);
            })
    }


    render() {
        return (
            <div className="App">
                <div className="App-header">
                    <h2>Welcome to React</h2>
                </div>
                {JSON.stringify(this.state.receivedData)}
            </div>
        );
    }
}

export default App;

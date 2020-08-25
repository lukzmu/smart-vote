import React, {Component} from 'react';
import Votings from './components/votings';

    class App extends Component {
      state = {
        votings: []
      }

      componentDidMount() {
        fetch('http://ec2-34-244-59-141.eu-west-1.compute.amazonaws.com:8000/voting')
        .then(res => res.json())
        .then((data) => {
          this.setState({ votings: data })
        })
        .catch(console.log)
      }

      render () {
        return (
          <Votings votings={this.state.votings} />
        );
      }
    }

    export default App;
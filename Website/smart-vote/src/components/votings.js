import React from 'react'

    const Votings = ({ votings }) => {
      return (
        <div className="row">
          {votings.map((voting) => (
            <div className="col-sm-6 col-md-4">
                <div className="vote-box">
                    <img src={voting.image}/>
                    <div className="description">
                        <h1 className="float-left">{voting.name}</h1>
                        <span>{voting.category}</span>
                        <p>
                            {voting.description}
                        </p>
                        <button type="button" className="btn btn-danger btn-lg btn-block  bg-smartvote">Zagłosuj</button>
                    </div>
                </div>
            </div>
          ))}
        </div>
      )
    };

    export default Votings
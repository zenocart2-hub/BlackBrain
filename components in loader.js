import React from "react";

/*
  Loader Component
  ----------------
  Simple reusable loader
*/

const Loader = ({ text = "Loading..." }) => {
  return (
    <div className="loader">
      {text}
    </div>
  );
};

export default Loader;
import { useEffect, useState } from 'react'
import './App.css'
import { Button } from 'flowbite-react';

function App() {
  const [fucksGiven, setFucksGiven] = useState(0);

  useEffect(() => {
    setFucksGiven(2);
  }, [])

  return (
    <>
      <h1>Hello World!</h1>
      <p>fucks given: {fucksGiven}</p>
      <Button color="alternative" pill>
        Alternative
      </Button>
    </>
  )
}

export default App

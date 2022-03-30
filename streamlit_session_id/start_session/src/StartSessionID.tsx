import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import { uuid } from 'uuidv4'
import { ReactNode } from "react"

class StartSessionIDComponent extends StreamlitComponentBase<any> {
  public state = { status: true }

  public render = (): ReactNode => {

    let session_id = localStorage.getItem('session_id')

    console.log(session_id)

    if (session_id === null) {
      let myuuid = uuid()
      localStorage.setItem('session_id', myuuid)
      session_id = localStorage.getItem('session_id')
    }
    Streamlit.setComponentValue(session_id)

    return null
  }

}

export default withStreamlitConnection(StartSessionIDComponent)

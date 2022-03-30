import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import { ReactNode } from "react"

class ClearAllComponent extends StreamlitComponentBase<any> {
  public state = { numClicks: 0, isFocused: false }

  public render = (): ReactNode => {

    localStorage.clear()
    
    return null
  }

}

export default withStreamlitConnection(ClearAllComponent)
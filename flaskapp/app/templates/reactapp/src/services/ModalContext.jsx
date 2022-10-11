import Modal from "components/Modal";
import React, { createContext, useContext, useEffect, useState } from "react";
import ReactDOM from "react-dom";
import { v4 as uuidv4 } from "uuid";

const Context = createContext(null);
const modalRoot = document.getElementById("modals");

const ModalContextProvider = ({ children }) => {
  const [modais, setModais] = useState([]);
  const rootElemRef = React.useRef(document.createElement("div"));

  useEffect(() => {
    if (modalRoot) {
      modalRoot.appendChild(rootElemRef.current);
    }
    return function removeElement() {
      rootElemRef.current.remove();
    };
  }, []);

  function templateRemoveModal({ hook, id }) {
    const newModais = modais.filter((modal) => modal.id !== id);
    setModais(newModais);
    hook();
  }

  function addModal({
    confirmButtonAction = () => {},
    content,
    returnButtonAction = () => {},
    title,
  }) {
    const id = uuidv4();
    setModais([
      ...modais,
      {
        id,
        tag: (
          <Modal
            key={id}
            headerTitle={title}
            confirmButton={() =>
              templateRemoveModal({
                hook: confirmButtonAction,
                id,
              })
            }
            goBack={() =>
              templateRemoveModal({
                hook: returnButtonAction,
                id,
              })
            }
          >
            {content}
          </Modal>
        ),
      },
    ]);
  }

  return (
    <Context.Provider value={{ addModal }}>
      {ReactDOM.createPortal(
        <>{modais.map((modal) => modal.tag)}</>,
        rootElemRef.current
      )}
      {children}
    </Context.Provider>
  );
};

export const useModalContext = () => useContext(Context);

export default ModalContextProvider;

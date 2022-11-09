# import required module
import os
# assign directory

path = input('Enter the path of the react directory : ')

directory = r'%s' % path



targets_folders = ['public', 'src']
delete_files = {
    'src': ['App.test.js', 'index.css', 'logo.svg', 'reportWebVitals.js', 'setupTests.js'],
    'public': ['favicon.ico', 'logo192.png', 'logo512.png', 'manifest.json', 'robots.txt']
}

updated_files = {
    'index.js': """
            import React from 'react';
            import ReactDOM from 'react-dom/client';
            import App from './App';

            const root = ReactDOM.createRoot(document.getElementById('root'));
            root.render(
            <React.StrictMode>
                <App />
            </React.StrictMode>
            );
            """,
    'App.js': """
            import './App.css';

            function App() {
            return (
                <div className="App">
                Hello React!
                </div>
            );
            }

            export default App;
            """,
    'App.css': """
            .App {
            text-align: center;
            }
            """
}

confirm = input('confirm deleting and editing files (y/n) : ')

if (confirm == 'y' or confirm == 'y'.upper()) or (confirm == 'yes' or confirm == 'yes'.upper()):
    for f in os.listdir(directory):
        if f in targets_folders:
            folders = os.path.join(directory, f)
            #print(folders) returns the public src with their path
            for file in os.listdir(folders):
                # print(os.path.join(folders,file))
                if (file in delete_files['src']) or (file in delete_files['public']):
                    # print(os.path.join(folders,file))
                    os.remove(os.path.join(folders, file))
                    print(f'removing {file} ...')

                elif file in updated_files:
                    with open(os.path.join(folders, file), 'w') as e:
                        content = updated_files[file]
                        e.write(content)
                        print(f'editing {file} ...')

    print('Done.')


else:
    print('Exit..')

# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.14</td>
    <td align="right">6.56</td>
    <td align="right">4.55</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.44</td>
    <td align="right">11.69</td>
    <td align="right">18.00</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.85</td>
    <td align="right">4.59</td>
    <td align="right">4.59</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.71</td>
    <td align="right">4.98</td>
    <td align="right">4.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">19.58</td>
    <td align="right">17.04</td>
    <td align="right">18.84</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.41</td>
    <td align="right">5.05</td>
    <td align="right">5.05</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.22</td>
    <td align="right">5.48</td>
    <td align="right">5.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">22.64</td>
    <td align="right">19.91</td>
    <td align="right">17.69</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.99</td>
    <td align="right">5.30</td>
    <td align="right">5.29</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.85</td>
    <td align="right">5.94</td>
    <td align="right">5.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">28.85</td>
    <td align="right">25.08</td>
    <td align="right">18.12</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.58</td>
    <td align="right">5.77</td>
    <td align="right">5.77</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.26</td>
    <td align="right">6.26</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.19</td>
    <td align="right">5.51</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.47</td>
    <td align="right">6.68</td>
    <td align="right">6.69</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.27</td>
    <td align="right">3.40</td>
    <td align="right">3.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.08</td>
    <td align="right">7.76</td>
    <td align="right">7.75</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.19</td>
    <td align="right">10.14</td>
    <td align="right">10.14</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.56</td>
    <td align="right">3.09</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.18</td>
    <td align="right">11.33</td>
    <td align="right">11.34</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">22.41</td>
    <td align="right">13.40</td>
    <td align="right">13.32</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">6.16</td>
    <td align="right">5.86</td>
    <td align="right">4.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.33</td>
    <td align="right">13.10</td>
    <td align="right">13.12</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.29</td>
    <td align="right">15.92</td>
    <td align="right">15.81</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">6.22</td>
    <td align="right">5.89</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.21</td>
    <td align="right">3.21</td>
    <td align="right">3.21</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.61</td>
    <td align="right">5.34</td>
    <td align="right">5.21</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.67</td>
    <td align="right">5.01</td>
    <td align="right">5.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.34</td>
    <td align="right">3.32</td>
    <td align="right">3.29</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.47</td>
    <td align="right">4.47</td>
    <td align="right">4.46</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.74</td>
    <td align="right">5.17</td>
    <td align="right">5.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.61</td>
    <td align="right">5.51</td>
    <td align="right">3.91</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.53</td>
    <td align="right">8.13</td>
    <td align="right">6.26</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.87</td>
    <td align="right">7.92</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.65</td>
    <td align="right">5.56</td>
    <td align="right">3.95</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">9.09</td>
    <td align="right">9.43</td>
    <td align="right">6.20</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.89</td>
    <td align="right">8.99</td>
    <td align="right">6.12</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.19</td>
    <td align="right">7.67</td>
    <td align="right">15.03</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.38</td>
    <td align="right">9.74</td>
    <td align="right">19.32</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.77</td>
    <td align="right">10.86</td>
    <td align="right">10.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.81</td>
    <td align="right">9.81</td>
    <td align="right">13.81</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.09</td>
    <td align="right">10.19</td>
    <td align="right">15.58</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.67</td>
    <td align="right">13.61</td>
    <td align="right">14.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.88</td>
    <td align="right">11.38</td>
    <td align="right">13.43</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.76</td>
    <td align="right">12.63</td>
    <td align="right">16.67</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.59</td>
    <td align="right">16.25</td>
    <td align="right">16.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">13.31</td>
    <td align="right">13.93</td>
    <td align="right">14.78</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.07</td>
    <td align="right">14.81</td>
    <td align="right">16.16</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">20.92</td>
    <td align="right">21.07</td>
    <td align="right">21.06</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">48.46</td>
    <td align="right">24.27</td>
    <td align="right">15.06</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">16.12</td>
    <td align="right">13.64</td>
    <td align="right">19.95</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.42</td>
    <td align="right">6.24</td>
    <td align="right">6.39</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">6.16</td>
    <td align="right">6.07</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">53.17</td>
    <td align="right">49.52</td>
    <td align="right">26.37</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.73</td>
    <td align="right">11.35</td>
    <td align="right">11.35</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">12.00</td>
    <td align="right">12.33</td>
    <td align="right">12.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">88.02</td>
    <td align="right">83.08</td>
    <td align="right">31.32</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.60</td>
    <td align="right">18.11</td>
    <td align="right">18.10</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">18.94</td>
    <td align="right">18.88</td>
    <td align="right">18.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">126.46</td>
    <td align="right">115.82</td>
    <td align="right">36.40</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.82</td>
    <td align="right">21.80</td>
    <td align="right">21.80</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">25.54</td>
    <td align="right">22.66</td>
    <td align="right">22.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.88</td>
    <td align="right">6.25</td>
    <td align="right">6.26</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.44</td>
    <td align="right">7.88</td>
    <td align="right">7.87</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.97</td>
    <td align="right">4.28</td>
    <td align="right">4.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">15.13</td>
    <td align="right">15.52</td>
    <td align="right">15.52</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">18.77</td>
    <td align="right">21.64</td>
    <td align="right">21.57</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.12</td>
    <td align="right">8.08</td>
    <td align="right">8.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">30.28</td>
    <td align="right">30.47</td>
    <td align="right">30.46</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">38.03</td>
    <td align="right">33.37</td>
    <td align="right">33.36</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">19.40</td>
    <td align="right">20.39</td>
    <td align="right">14.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">39.37</td>
    <td align="right">38.97</td>
    <td align="right">39.00</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">41.22</td>
    <td align="right">51.05</td>
    <td align="right">51.01</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">22.36</td>
    <td align="right">23.38</td>
    <td align="right">16.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">4.19</td>
    <td align="right">4.36</td>
    <td align="right">4.42</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.50</td>
    <td align="right">6.26</td>
    <td align="right">6.13</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">6.70</td>
    <td align="right">7.28</td>
    <td align="right">7.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">8.08</td>
    <td align="right">8.89</td>
    <td align="right">8.85</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">8.47</td>
    <td align="right">10.05</td>
    <td align="right">10.39</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">9.84</td>
    <td align="right">11.51</td>
    <td align="right">11.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">17.87</td>
    <td align="right">18.68</td>
    <td align="right">14.47</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.74</td>
    <td align="right">26.11</td>
    <td align="right">21.47</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">25.67</td>
    <td align="right">25.97</td>
    <td align="right">20.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">20.85</td>
    <td align="right">21.32</td>
    <td align="right">16.24</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">32.44</td>
    <td align="right">35.83</td>
    <td align="right">24.86</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.87</td>
    <td align="right">33.25</td>
    <td align="right">24.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.92</td>
    <td align="right">9.47</td>
    <td align="right">16.36</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.66</td>
    <td align="right">11.67</td>
    <td align="right">23.12</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">14.39</td>
    <td align="right">13.90</td>
    <td align="right">13.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">17.86</td>
    <td align="right">17.04</td>
    <td align="right">17.74</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">23.62</td>
    <td align="right">21.58</td>
    <td align="right">20.17</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">31.72</td>
    <td align="right">31.88</td>
    <td align="right">31.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">27.35</td>
    <td align="right">27.25</td>
    <td align="right">21.09</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">39.18</td>
    <td align="right">33.28</td>
    <td align="right">25.10</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">48.31</td>
    <td align="right">50.89</td>
    <td align="right">50.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">41.40</td>
    <td align="right">41.72</td>
    <td align="right">24.49</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">51.94</td>
    <td align="right">50.44</td>
    <td align="right">27.70</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.66</td>
    <td align="right">73.76</td>
    <td align="right">73.89</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.27</td>
    <td align="right">5.84</td>
    <td align="right">4.30</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.52</td>
    <td align="right">10.63</td>
    <td align="right">17.12</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.59</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.12</td>
    <td align="right">4.66</td>
    <td align="right">4.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.68</td>
    <td align="right">15.38</td>
    <td align="right">18.42</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.15</td>
    <td align="right">4.67</td>
    <td align="right">4.67</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.68</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.89</td>
    <td align="right">18.68</td>
    <td align="right">17.06</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.65</td>
    <td align="right">5.06</td>
    <td align="right">5.07</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.99</td>
    <td align="right">5.95</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.86</td>
    <td align="right">23.19</td>
    <td align="right">17.51</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.00</td>
    <td align="right">5.61</td>
    <td align="right">5.61</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">3.30</td>
    <td align="right">3.50</td>
    <td align="right">3.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.34</td>
    <td align="right">3.90</td>
    <td align="right">3.90</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.36</td>
    <td align="right">3.76</td>
    <td align="right">3.76</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.79</td>
    <td align="right">2.54</td>
    <td align="right">2.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.05</td>
    <td align="right">4.75</td>
    <td align="right">4.76</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.01</td>
    <td align="right">4.90</td>
    <td align="right">4.89</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.28</td>
    <td align="right">2.31</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">6.01</td>
    <td align="right">7.83</td>
    <td align="right">7.84</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">6.14</td>
    <td align="right">7.56</td>
    <td align="right">7.56</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.41</td>
    <td align="right">4.35</td>
    <td align="right">3.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.53</td>
    <td align="right">8.48</td>
    <td align="right">8.48</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">7.06</td>
    <td align="right">8.70</td>
    <td align="right">8.69</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.45</td>
    <td align="right">4.38</td>
    <td align="right">3.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.78</td>
    <td align="right">2.35</td>
    <td align="right">2.36</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.91</td>
    <td align="right">4.14</td>
    <td align="right">4.13</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.97</td>
    <td align="right">3.96</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.90</td>
    <td align="right">2.42</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.22</td>
    <td align="right">3.83</td>
    <td align="right">3.83</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.17</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.51</td>
    <td align="right">4.32</td>
    <td align="right">3.05</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.86</td>
    <td align="right">6.33</td>
    <td align="right">5.06</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">6.10</td>
    <td align="right">6.16</td>
    <td align="right">4.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.57</td>
    <td align="right">4.32</td>
    <td align="right">3.02</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.01</td>
    <td align="right">7.18</td>
    <td align="right">5.09</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">7.29</td>
    <td align="right">6.92</td>
    <td align="right">5.02</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.97</td>
    <td align="right">7.01</td>
    <td align="right">13.88</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.82</td>
    <td align="right">8.19</td>
    <td align="right">18.58</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.60</td>
    <td align="right">11.14</td>
    <td align="right">11.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.46</td>
    <td align="right">9.60</td>
    <td align="right">13.72</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.56</td>
    <td align="right">9.99</td>
    <td align="right">15.70</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.54</td>
    <td align="right">15.04</td>
    <td align="right">14.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.56</td>
    <td align="right">11.27</td>
    <td align="right">13.55</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">16.79</td>
    <td align="right">12.68</td>
    <td align="right">16.70</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.09</td>
    <td align="right">16.06</td>
    <td align="right">16.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">15.19</td>
    <td align="right">13.59</td>
    <td align="right">14.01</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">18.53</td>
    <td align="right">14.81</td>
    <td align="right">16.21</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">22.88</td>
    <td align="right">20.97</td>
    <td align="right">21.14</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">50.60</td>
    <td align="right">23.65</td>
    <td align="right">14.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">12.86</td>
    <td align="right">13.83</td>
    <td align="right">19.67</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.71</td>
    <td align="right">5.29</td>
    <td align="right">5.30</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.08</td>
    <td align="right">5.77</td>
    <td align="right">5.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">39.66</td>
    <td align="right">41.29</td>
    <td align="right">24.87</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.06</td>
    <td align="right">9.80</td>
    <td align="right">9.79</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.28</td>
    <td align="right">12.59</td>
    <td align="right">12.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">71.49</td>
    <td align="right">74.21</td>
    <td align="right">30.07</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.09</td>
    <td align="right">17.35</td>
    <td align="right">17.37</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">17.00</td>
    <td align="right">20.72</td>
    <td align="right">20.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">103.68</td>
    <td align="right">103.40</td>
    <td align="right">34.97</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.31</td>
    <td align="right">21.46</td>
    <td align="right">21.46</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.56</td>
    <td align="right">15.22</td>
    <td align="right">15.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.51</td>
    <td align="right">6.24</td>
    <td align="right">6.25</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.15</td>
    <td align="right">4.66</td>
    <td align="right">4.66</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">4.76</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.88</td>
    <td align="right">10.12</td>
    <td align="right">10.11</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.19</td>
    <td align="right">11.71</td>
    <td align="right">11.71</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.33</td>
    <td align="right">6.57</td>
    <td align="right">6.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.71</td>
    <td align="right">22.59</td>
    <td align="right">22.60</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.96</td>
    <td align="right">22.54</td>
    <td align="right">22.56</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.84</td>
    <td align="right">16.05</td>
    <td align="right">11.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">24.28</td>
    <td align="right">30.19</td>
    <td align="right">30.18</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.74</td>
    <td align="right">31.13</td>
    <td align="right">31.15</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.95</td>
    <td align="right">17.98</td>
    <td align="right">13.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.94</td>
    <td align="right">3.68</td>
    <td align="right">3.67</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.01</td>
    <td align="right">5.33</td>
    <td align="right">5.29</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.86</td>
    <td align="right">4.87</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">7.26</td>
    <td align="right">7.43</td>
    <td align="right">7.95</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">8.19</td>
    <td align="right">9.39</td>
    <td align="right">9.36</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">10.76</td>
    <td align="right">12.29</td>
    <td align="right">12.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">15.09</td>
    <td align="right">16.28</td>
    <td align="right">11.84</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.91</td>
    <td align="right">21.54</td>
    <td align="right">17.08</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">19.66</td>
    <td align="right">21.04</td>
    <td align="right">16.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">17.31</td>
    <td align="right">18.25</td>
    <td align="right">13.20</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">25.10</td>
    <td align="right">27.04</td>
    <td align="right">19.62</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">25.37</td>
    <td align="right">26.93</td>
    <td align="right">19.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.89</td>
    <td align="right">8.82</td>
    <td align="right">15.60</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">14.08</td>
    <td align="right">10.36</td>
    <td align="right">20.38</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">12.67</td>
    <td align="right">13.34</td>
    <td align="right">13.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">17.99</td>
    <td align="right">17.76</td>
    <td align="right">18.38</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">21.20</td>
    <td align="right">19.23</td>
    <td align="right">19.45</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">29.53</td>
    <td align="right">30.19</td>
    <td align="right">30.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">27.98</td>
    <td align="right">27.14</td>
    <td align="right">21.78</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">42.08</td>
    <td align="right">33.11</td>
    <td align="right">25.15</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">46.90</td>
    <td align="right">47.14</td>
    <td align="right">47.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">44.00</td>
    <td align="right">41.31</td>
    <td align="right">24.26</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">53.58</td>
    <td align="right">50.18</td>
    <td align="right">27.22</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">80.12</td>
    <td align="right">73.52</td>
    <td align="right">73.45</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.67</td>
    <td align="right">2.44</td>
    <td align="right">1.97</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">6.30</td>
    <td align="right">4.45</td>
    <td align="right">11.38</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.31</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.62</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">9.44</td>
    <td align="right">6.62</td>
    <td align="right">11.76</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.37</td>
    <td align="right">1.34</td>
    <td align="right">1.33</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.68</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">12.42</td>
    <td align="right">8.15</td>
    <td align="right">10.97</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.52</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.73</td>
    <td align="right">1.56</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">15.43</td>
    <td align="right">10.77</td>
    <td align="right">11.26</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.71</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.79</td>
    <td align="right">1.56</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.29</td>
    <td align="right">1.74</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.27</td>
    <td align="right">1.77</td>
    <td align="right">1.76</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.01</td>
    <td align="right">1.70</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.15</td>
    <td align="right">1.85</td>
    <td align="right">1.84</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.70</td>
    <td align="right">2.13</td>
    <td align="right">2.22</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.49</td>
    <td align="right">1.34</td>
    <td align="right">1.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.14</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.03</td>
    <td align="right">3.02</td>
    <td align="right">3.03</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">2.97</td>
    <td align="right">2.39</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.60</td>
    <td align="right">3.40</td>
    <td align="right">3.36</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.69</td>
    <td align="right">3.59</td>
    <td align="right">3.60</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">2.92</td>
    <td align="right">2.91</td>
    <td align="right">1.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.02</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.27</td>
    <td align="right">1.74</td>
    <td align="right">1.73</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.27</td>
    <td align="right">1.76</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.03</td>
    <td align="right">1.61</td>
    <td align="right">1.61</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.16</td>
    <td align="right">1.85</td>
    <td align="right">1.86</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.73</td>
    <td align="right">2.14</td>
    <td align="right">2.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">2.88</td>
    <td align="right">2.39</td>
    <td align="right">1.75</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.12</td>
    <td align="right">2.93</td>
    <td align="right">2.94</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.10</td>
    <td align="right">3.03</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">2.98</td>
    <td align="right">2.90</td>
    <td align="right">1.76</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.59</td>
    <td align="right">3.43</td>
    <td align="right">3.42</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.80</td>
    <td align="right">3.61</td>
    <td align="right">3.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">3.13</td>
    <td align="right">3.19</td>
    <td align="right">10.17</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">7.04</td>
    <td align="right">3.94</td>
    <td align="right">12.64</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">7.73</td>
    <td align="right">4.89</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">4.27</td>
    <td align="right">4.28</td>
    <td align="right">9.85</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">7.45</td>
    <td align="right">4.57</td>
    <td align="right">10.47</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">10.88</td>
    <td align="right">6.78</td>
    <td align="right">6.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">5.38</td>
    <td align="right">5.17</td>
    <td align="right">9.61</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">8.52</td>
    <td align="right">5.74</td>
    <td align="right">11.20</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">12.04</td>
    <td align="right">7.56</td>
    <td align="right">7.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">6.84</td>
    <td align="right">6.22</td>
    <td align="right">10.04</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">9.36</td>
    <td align="right">6.36</td>
    <td align="right">10.70</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">17.66</td>
    <td align="right">10.64</td>
    <td align="right">10.62</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.50</td>
    <td align="right">10.93</td>
    <td align="right">6.29</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">7.76</td>
    <td align="right">6.23</td>
    <td align="right">12.83</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">1.95</td>
    <td align="right">1.87</td>
    <td align="right">1.86</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.10</td>
    <td align="right">2.00</td>
    <td align="right">2.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">13.11</td>
    <td align="right">11.19</td>
    <td align="right">15.72</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">3.32</td>
    <td align="right">3.18</td>
    <td align="right">3.24</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">3.18</td>
    <td align="right">3.17</td>
    <td align="right">3.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">29.94</td>
    <td align="right">24.95</td>
    <td align="right">18.16</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.76</td>
    <td align="right">6.06</td>
    <td align="right">6.11</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.63</td>
    <td align="right">6.42</td>
    <td align="right">5.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">55.31</td>
    <td align="right">40.47</td>
    <td align="right">20.75</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">9.01</td>
    <td align="right">7.98</td>
    <td align="right">7.63</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.37</td>
    <td align="right">6.22</td>
    <td align="right">6.31</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.68</td>
    <td align="right">2.49</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.71</td>
    <td align="right">2.58</td>
    <td align="right">2.58</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.39</td>
    <td align="right">2.47</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.56</td>
    <td align="right">4.23</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.23</td>
    <td align="right">4.55</td>
    <td align="right">4.52</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.80</td>
    <td align="right">3.48</td>
    <td align="right">3.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.76</td>
    <td align="right">9.51</td>
    <td align="right">9.51</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">10.67</td>
    <td align="right">9.82</td>
    <td align="right">9.82</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.49</td>
    <td align="right">8.06</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.32</td>
    <td align="right">12.23</td>
    <td align="right">12.29</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.33</td>
    <td align="right">12.93</td>
    <td align="right">14.03</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.34</td>
    <td align="right">11.03</td>
    <td align="right">6.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">2.39</td>
    <td align="right">2.51</td>
    <td align="right">2.48</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.70</td>
    <td align="right">2.51</td>
    <td align="right">2.51</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.72</td>
    <td align="right">2.58</td>
    <td align="right">2.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.84</td>
    <td align="right">2.92</td>
    <td align="right">3.03</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.70</td>
    <td align="right">3.99</td>
    <td align="right">3.92</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.16</td>
    <td align="right">4.62</td>
    <td align="right">4.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">8.49</td>
    <td align="right">8.24</td>
    <td align="right">5.94</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.70</td>
    <td align="right">9.78</td>
    <td align="right">9.63</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">10.78</td>
    <td align="right">9.79</td>
    <td align="right">9.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.82</td>
    <td align="right">11.14</td>
    <td align="right">6.28</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.30</td>
    <td align="right">12.95</td>
    <td align="right">13.12</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.61</td>
    <td align="right">13.53</td>
    <td align="right">14.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">4.46</td>
    <td align="right">4.13</td>
    <td align="right">11.14</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">8.73</td>
    <td align="right">4.85</td>
    <td align="right">13.35</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">8.87</td>
    <td align="right">6.68</td>
    <td align="right">6.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">9.18</td>
    <td align="right">8.28</td>
    <td align="right">12.81</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.18</td>
    <td align="right">7.82</td>
    <td align="right">12.70</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">14.54</td>
    <td align="right">12.08</td>
    <td align="right">12.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">16.27</td>
    <td align="right">13.78</td>
    <td align="right">14.03</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">21.55</td>
    <td align="right">15.67</td>
    <td align="right">16.51</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">26.66</td>
    <td align="right">22.08</td>
    <td align="right">22.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">22.31</td>
    <td align="right">17.88</td>
    <td align="right">15.17</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">30.95</td>
    <td align="right">21.22</td>
    <td align="right">17.14</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">50.16</td>
    <td align="right">38.17</td>
    <td align="right">39.03</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.17</td>
    <td align="right">5.13</td>
    <td align="right">3.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.23</td>
    <td align="right">10.52</td>
    <td align="right">14.04</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.70</td>
    <td align="right">3.43</td>
    <td align="right">3.41</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.26</td>
    <td align="right">4.08</td>
    <td align="right">4.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.54</td>
    <td align="right">14.84</td>
    <td align="right">14.79</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.31</td>
    <td align="right">3.86</td>
    <td align="right">3.86</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.94</td>
    <td align="right">4.74</td>
    <td align="right">4.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.21</td>
    <td align="right">18.05</td>
    <td align="right">13.80</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.40</td>
    <td align="right">4.27</td>
    <td align="right">4.25</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.56</td>
    <td align="right">5.10</td>
    <td align="right">5.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.26</td>
    <td align="right">22.89</td>
    <td align="right">13.99</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.84</td>
    <td align="right">4.64</td>
    <td align="right">4.63</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">8.24</td>
    <td align="right">5.52</td>
    <td align="right">5.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.29</td>
    <td align="right">4.23</td>
    <td align="right">4.23</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">7.87</td>
    <td align="right">4.54</td>
    <td align="right">4.55</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.85</td>
    <td align="right">2.10</td>
    <td align="right">2.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.18</td>
    <td align="right">6.94</td>
    <td align="right">6.78</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.94</td>
    <td align="right">6.87</td>
    <td align="right">6.76</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.77</td>
    <td align="right">2.91</td>
    <td align="right">2.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.54</td>
    <td align="right">9.32</td>
    <td align="right">9.31</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">12.34</td>
    <td align="right">10.43</td>
    <td align="right">10.13</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.84</td>
    <td align="right">4.38</td>
    <td align="right">3.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.53</td>
    <td align="right">10.18</td>
    <td align="right">10.12</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">14.31</td>
    <td align="right">12.21</td>
    <td align="right">12.02</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.31</td>
    <td align="right">4.39</td>
    <td align="right">3.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.84</td>
    <td align="right">1.90</td>
    <td align="right">1.90</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.71</td>
    <td align="right">3.19</td>
    <td align="right">3.18</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.77</td>
    <td align="right">3.00</td>
    <td align="right">3.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.25</td>
    <td align="right">3.18</td>
    <td align="right">2.57</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.17</td>
    <td align="right">3.78</td>
    <td align="right">3.20</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.02</td>
    <td align="right">4.49</td>
    <td align="right">3.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.38</td>
    <td align="right">4.17</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.78</td>
    <td align="right">6.36</td>
    <td align="right">4.87</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.26</td>
    <td align="right">6.17</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.43</td>
    <td align="right">4.70</td>
    <td align="right">3.31</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.38</td>
    <td align="right">6.84</td>
    <td align="right">4.86</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.73</td>
    <td align="right">6.71</td>
    <td align="right">4.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.91</td>
    <td align="right">6.53</td>
    <td align="right">11.24</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">9.70</td>
    <td align="right">8.80</td>
    <td align="right">13.93</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">9.98</td>
    <td align="right">8.89</td>
    <td align="right">8.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.74</td>
    <td align="right">12.66</td>
    <td align="right">13.19</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">11.52</td>
    <td align="right">10.94</td>
    <td align="right">13.01</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">13.80</td>
    <td align="right">12.77</td>
    <td align="right">12.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.32</td>
    <td align="right">11.28</td>
    <td align="right">11.65</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.07</td>
    <td align="right">13.13</td>
    <td align="right">12.51</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">17.93</td>
    <td align="right">15.16</td>
    <td align="right">15.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.70</td>
    <td align="right">31.70</td>
    <td align="right">21.52</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">16.04</td>
    <td align="right">14.83</td>
    <td align="right">12.14</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">31.23</td>
    <td align="right">22.47</td>
    <td align="right">22.39</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">43.44</td>
    <td align="right">23.72</td>
    <td align="right">16.30</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">9.95</td>
    <td align="right">11.03</td>
    <td align="right">15.44</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.14</td>
    <td align="right">3.79</td>
    <td align="right">3.67</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.66</td>
    <td align="right">4.46</td>
    <td align="right">4.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.57</td>
    <td align="right">58.05</td>
    <td align="right">25.13</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.66</td>
    <td align="right">6.24</td>
    <td align="right">6.22</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.71</td>
    <td align="right">6.29</td>
    <td align="right">6.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">65.22</td>
    <td align="right">72.60</td>
    <td align="right">24.46</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">15.10</td>
    <td align="right">13.07</td>
    <td align="right">13.10</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.10</td>
    <td align="right">15.90</td>
    <td align="right">15.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">96.10</td>
    <td align="right">109.07</td>
    <td align="right">29.44</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.37</td>
    <td align="right">16.50</td>
    <td align="right">16.48</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">20.31</td>
    <td align="right">22.40</td>
    <td align="right">22.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.96</td>
    <td align="right">4.58</td>
    <td align="right">4.58</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">8.27</td>
    <td align="right">4.91</td>
    <td align="right">4.95</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.19</td>
    <td align="right">2.36</td>
    <td align="right">2.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.24</td>
    <td align="right">8.57</td>
    <td align="right">8.48</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.19</td>
    <td align="right">8.79</td>
    <td align="right">8.66</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">4.74</td>
    <td align="right">4.54</td>
    <td align="right">4.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">25.75</td>
    <td align="right">23.35</td>
    <td align="right">23.50</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">29.62</td>
    <td align="right">28.11</td>
    <td align="right">28.22</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">13.93</td>
    <td align="right">15.28</td>
    <td align="right">10.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">35.40</td>
    <td align="right">34.46</td>
    <td align="right">34.52</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">39.62</td>
    <td align="right">37.72</td>
    <td align="right">37.60</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.24</td>
    <td align="right">17.81</td>
    <td align="right">12.31</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.17</td>
    <td align="right">2.12</td>
    <td align="right">2.10</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.12</td>
    <td align="right">3.43</td>
    <td align="right">3.46</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.19</td>
    <td align="right">3.26</td>
    <td align="right">3.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">5.03</td>
    <td align="right">5.04</td>
    <td align="right">4.17</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.89</td>
    <td align="right">5.27</td>
    <td align="right">4.76</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.63</td>
    <td align="right">6.26</td>
    <td align="right">5.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.86</td>
    <td align="right">15.32</td>
    <td align="right">10.86</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.54</td>
    <td align="right">18.83</td>
    <td align="right">15.74</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">23.30</td>
    <td align="right">18.60</td>
    <td align="right">15.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">17.80</td>
    <td align="right">17.79</td>
    <td align="right">12.21</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">29.11</td>
    <td align="right">26.38</td>
    <td align="right">18.72</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.74</td>
    <td align="right">24.44</td>
    <td align="right">18.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.51</td>
    <td align="right">15.79</td>
    <td align="right">16.55</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">10.28</td>
    <td align="right">9.57</td>
    <td align="right">14.69</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">12.01</td>
    <td align="right">9.89</td>
    <td align="right">9.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">11.04</td>
    <td align="right">12.06</td>
    <td align="right">13.40</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.97</td>
    <td align="right">13.66</td>
    <td align="right">14.20</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">15.36</td>
    <td align="right">13.93</td>
    <td align="right">13.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">25.41</td>
    <td align="right">24.86</td>
    <td align="right">19.11</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">32.73</td>
    <td align="right">32.09</td>
    <td align="right">19.61</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">39.10</td>
    <td align="right">38.00</td>
    <td align="right">38.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">35.49</td>
    <td align="right">34.85</td>
    <td align="right">22.79</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">41.64</td>
    <td align="right">40.54</td>
    <td align="right">21.82</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.43</td>
    <td align="right">64.53</td>
    <td align="right">64.42</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">73.91</td>
    <td align="right">37.42</td>
    <td align="right">14.30</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.45</td>
    <td align="right">43.40</td>
    <td align="right">37.59</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">13.43</td>
    <td align="right">17.75</td>
    <td align="right">17.94</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">17.14</td>
    <td align="right">20.01</td>
    <td align="right">20.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">41.97</td>
    <td align="right">68.21</td>
    <td align="right">40.14</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">18.37</td>
    <td align="right">21.45</td>
    <td align="right">21.27</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.09</td>
    <td align="right">18.90</td>
    <td align="right">18.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">50.95</td>
    <td align="right">84.05</td>
    <td align="right">39.85</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.52</td>
    <td align="right">19.19</td>
    <td align="right">19.24</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">17.31</td>
    <td align="right">21.05</td>
    <td align="right">21.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">64.45</td>
    <td align="right">105.49</td>
    <td align="right">39.95</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.55</td>
    <td align="right">20.65</td>
    <td align="right">20.74</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.18</td>
    <td align="right">21.91</td>
    <td align="right">22.89</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.36</td>
    <td align="right">22.66</td>
    <td align="right">22.56</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.54</td>
    <td align="right">26.30</td>
    <td align="right">27.07</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">12.45</td>
    <td align="right">15.73</td>
    <td align="right">15.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">26.02</td>
    <td align="right">29.48</td>
    <td align="right">29.61</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.27</td>
    <td align="right">32.50</td>
    <td align="right">32.47</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">14.31</td>
    <td align="right">17.68</td>
    <td align="right">17.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.88</td>
    <td align="right">35.64</td>
    <td align="right">35.55</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.80</td>
    <td align="right">48.99</td>
    <td align="right">49.15</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">16.70</td>
    <td align="right">20.68</td>
    <td align="right">20.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.87</td>
    <td align="right">39.94</td>
    <td align="right">40.10</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.53</td>
    <td align="right">58.28</td>
    <td align="right">58.09</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">24.29</td>
    <td align="right">25.00</td>
    <td align="right">25.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">14.39</td>
    <td align="right">15.97</td>
    <td align="right">15.98</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.39</td>
    <td align="right">22.62</td>
    <td align="right">22.63</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.55</td>
    <td align="right">26.43</td>
    <td align="right">26.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.30</td>
    <td align="right">19.44</td>
    <td align="right">19.44</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.81</td>
    <td align="right">29.50</td>
    <td align="right">29.63</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.24</td>
    <td align="right">32.49</td>
    <td align="right">32.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">22.98</td>
    <td align="right">23.78</td>
    <td align="right">23.83</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.92</td>
    <td align="right">35.61</td>
    <td align="right">35.54</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.90</td>
    <td align="right">49.04</td>
    <td align="right">49.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">31.59</td>
    <td align="right">32.74</td>
    <td align="right">32.60</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.89</td>
    <td align="right">39.94</td>
    <td align="right">40.07</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.50</td>
    <td align="right">58.22</td>
    <td align="right">58.06</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.85</td>
    <td align="right">24.47</td>
    <td align="right">27.27</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">32.79</td>
    <td align="right">29.99</td>
    <td align="right">35.89</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">31.98</td>
    <td align="right">34.25</td>
    <td align="right">34.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">31.40</td>
    <td align="right">38.26</td>
    <td align="right">29.16</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">45.85</td>
    <td align="right">39.56</td>
    <td align="right">32.86</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">43.02</td>
    <td align="right">44.60</td>
    <td align="right">44.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">37.62</td>
    <td align="right">44.99</td>
    <td align="right">28.16</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.33</td>
    <td align="right">47.71</td>
    <td align="right">34.32</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">44.42</td>
    <td align="right">47.19</td>
    <td align="right">46.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">42.27</td>
    <td align="right">50.03</td>
    <td align="right">29.63</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">51.35</td>
    <td align="right">51.16</td>
    <td align="right">34.12</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">62.54</td>
    <td align="right">65.31</td>
    <td align="right">65.43</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">107.82</td>
    <td align="right">126.19</td>
    <td align="right">27.26</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">33.92</td>
    <td align="right">53.88</td>
    <td align="right">45.05</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">15.14</td>
    <td align="right">20.84</td>
    <td align="right">20.42</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">19.65</td>
    <td align="right">24.51</td>
    <td align="right">24.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">92.50</td>
    <td align="right">132.14</td>
    <td align="right">60.46</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">27.73</td>
    <td align="right">34.65</td>
    <td align="right">34.44</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">25.26</td>
    <td align="right">29.47</td>
    <td align="right">29.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">179.45</td>
    <td align="right">251.78</td>
    <td align="right">79.17</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.19</td>
    <td align="right">41.47</td>
    <td align="right">45.70</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">39.95</td>
    <td align="right">50.08</td>
    <td align="right">50.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">267.47</td>
    <td align="right">402.48</td>
    <td align="right">97.48</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">47.61</td>
    <td align="right">61.75</td>
    <td align="right">62.22</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">61.26</td>
    <td align="right">63.24</td>
    <td align="right">64.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">23.31</td>
    <td align="right">26.57</td>
    <td align="right">26.69</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">27.91</td>
    <td align="right">31.77</td>
    <td align="right">31.53</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">14.60</td>
    <td align="right">19.28</td>
    <td align="right">18.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">41.76</td>
    <td align="right">43.81</td>
    <td align="right">43.89</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">52.90</td>
    <td align="right">45.66</td>
    <td align="right">45.73</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">22.75</td>
    <td align="right">27.50</td>
    <td align="right">26.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">64.57</td>
    <td align="right">69.26</td>
    <td align="right">69.43</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">101.97</td>
    <td align="right">82.32</td>
    <td align="right">82.58</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">41.46</td>
    <td align="right">45.12</td>
    <td align="right">45.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.50</td>
    <td align="right">92.83</td>
    <td align="right">92.99</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">134.13</td>
    <td align="right">107.96</td>
    <td align="right">107.89</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">68.98</td>
    <td align="right">73.38</td>
    <td align="right">73.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">18.39</td>
    <td align="right">19.82</td>
    <td align="right">19.48</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">23.34</td>
    <td align="right">26.72</td>
    <td align="right">26.68</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">28.32</td>
    <td align="right">32.01</td>
    <td align="right">31.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">28.83</td>
    <td align="right">30.64</td>
    <td align="right">30.94</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">39.43</td>
    <td align="right">43.93</td>
    <td align="right">44.17</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">54.13</td>
    <td align="right">47.18</td>
    <td align="right">47.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">53.49</td>
    <td align="right">47.68</td>
    <td align="right">47.59</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">64.62</td>
    <td align="right">69.88</td>
    <td align="right">69.80</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">101.82</td>
    <td align="right">80.76</td>
    <td align="right">80.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">80.67</td>
    <td align="right">86.48</td>
    <td align="right">85.06</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">86.91</td>
    <td align="right">91.63</td>
    <td align="right">91.75</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">134.39</td>
    <td align="right">108.77</td>
    <td align="right">108.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">21.03</td>
    <td align="right">28.74</td>
    <td align="right">31.09</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">36.75</td>
    <td align="right">36.58</td>
    <td align="right">40.61</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">40.60</td>
    <td align="right">39.17</td>
    <td align="right">40.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">45.32</td>
    <td align="right">48.99</td>
    <td align="right">36.81</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">58.42</td>
    <td align="right">56.67</td>
    <td align="right">43.86</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">62.53</td>
    <td align="right">65.49</td>
    <td align="right">65.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">66.59</td>
    <td align="right">74.50</td>
    <td align="right">47.46</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">85.90</td>
    <td align="right">85.19</td>
    <td align="right">58.00</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">92.25</td>
    <td align="right">95.24</td>
    <td align="right">95.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">84.14</td>
    <td align="right">91.51</td>
    <td align="right">56.78</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">102.53</td>
    <td align="right">104.91</td>
    <td align="right">66.26</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">143.71</td>
    <td align="right">139.85</td>
    <td align="right">142.16</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.91</td>
    <td align="right">14.92</td>
    <td align="right">8.57</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">15.87</td>
    <td align="right">22.99</td>
    <td align="right">28.11</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.09</td>
    <td align="right">13.43</td>
    <td align="right">13.43</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">14.87</td>
    <td align="right">16.33</td>
    <td align="right">16.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">22.31</td>
    <td align="right">33.90</td>
    <td align="right">28.76</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">15.33</td>
    <td align="right">16.74</td>
    <td align="right">16.62</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">17.14</td>
    <td align="right">18.81</td>
    <td align="right">18.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">27.87</td>
    <td align="right">42.30</td>
    <td align="right">29.41</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.59</td>
    <td align="right">19.18</td>
    <td align="right">19.17</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">20.68</td>
    <td align="right">21.60</td>
    <td align="right">21.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">35.67</td>
    <td align="right">53.19</td>
    <td align="right">29.94</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">21.06</td>
    <td align="right">22.03</td>
    <td align="right">22.03</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">23.28</td>
    <td align="right">24.37</td>
    <td align="right">24.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.28</td>
    <td align="right">17.02</td>
    <td align="right">17.02</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.14</td>
    <td align="right">17.19</td>
    <td align="right">17.18</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.82</td>
    <td align="right">8.69</td>
    <td align="right">8.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.98</td>
    <td align="right">25.95</td>
    <td align="right">25.95</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.27</td>
    <td align="right">26.08</td>
    <td align="right">26.06</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.07</td>
    <td align="right">12.39</td>
    <td align="right">12.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.29</td>
    <td align="right">36.32</td>
    <td align="right">36.34</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.40</td>
    <td align="right">35.54</td>
    <td align="right">35.50</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.57</td>
    <td align="right">15.41</td>
    <td align="right">15.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.35</td>
    <td align="right">38.85</td>
    <td align="right">38.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.29</td>
    <td align="right">40.71</td>
    <td align="right">40.74</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">17.61</td>
    <td align="right">20.25</td>
    <td align="right">20.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">7.26</td>
    <td align="right">8.50</td>
    <td align="right">8.50</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.29</td>
    <td align="right">17.18</td>
    <td align="right">17.17</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.14</td>
    <td align="right">17.19</td>
    <td align="right">17.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.95</td>
    <td align="right">12.18</td>
    <td align="right">12.19</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.98</td>
    <td align="right">25.98</td>
    <td align="right">25.98</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.26</td>
    <td align="right">26.04</td>
    <td align="right">26.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.97</td>
    <td align="right">15.30</td>
    <td align="right">15.30</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.34</td>
    <td align="right">36.39</td>
    <td align="right">36.38</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.38</td>
    <td align="right">35.48</td>
    <td align="right">35.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">17.51</td>
    <td align="right">19.06</td>
    <td align="right">19.07</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.37</td>
    <td align="right">38.84</td>
    <td align="right">38.85</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.28</td>
    <td align="right">40.68</td>
    <td align="right">40.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.06</td>
    <td align="right">18.09</td>
    <td align="right">22.48</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">47.41</td>
    <td align="right">40.62</td>
    <td align="right">40.81</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">26.24</td>
    <td align="right">29.33</td>
    <td align="right">27.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">26.62</td>
    <td align="right">27.57</td>
    <td align="right">23.25</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">51.55</td>
    <td align="right">45.48</td>
    <td align="right">38.78</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">36.34</td>
    <td align="right">35.33</td>
    <td align="right">35.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.28</td>
    <td align="right">34.92</td>
    <td align="right">23.30</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">59.57</td>
    <td align="right">53.33</td>
    <td align="right">40.26</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">39.30</td>
    <td align="right">38.00</td>
    <td align="right">37.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">38.41</td>
    <td align="right">45.36</td>
    <td align="right">28.04</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">63.30</td>
    <td align="right">57.30</td>
    <td align="right">42.24</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">51.24</td>
    <td align="right">49.49</td>
    <td align="right">49.47</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">123.61</td>
    <td align="right">61.61</td>
    <td align="right">23.23</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">25.99</td>
    <td align="right">34.34</td>
    <td align="right">34.12</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">14.58</td>
    <td align="right">15.98</td>
    <td align="right">16.06</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">15.92</td>
    <td align="right">17.22</td>
    <td align="right">17.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">56.72</td>
    <td align="right">70.72</td>
    <td align="right">38.99</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">25.52</td>
    <td align="right">25.17</td>
    <td align="right">25.17</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">27.25</td>
    <td align="right">31.44</td>
    <td align="right">31.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">110.29</td>
    <td align="right">151.51</td>
    <td align="right">56.81</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.30</td>
    <td align="right">44.78</td>
    <td align="right">44.75</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">49.79</td>
    <td align="right">49.14</td>
    <td align="right">49.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">163.66</td>
    <td align="right">237.86</td>
    <td align="right">71.79</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">62.83</td>
    <td align="right">63.76</td>
    <td align="right">63.84</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">66.67</td>
    <td align="right">67.51</td>
    <td align="right">67.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">21.83</td>
    <td align="right">21.57</td>
    <td align="right">21.45</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">19.50</td>
    <td align="right">20.89</td>
    <td align="right">20.84</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">9.39</td>
    <td align="right">10.38</td>
    <td align="right">10.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">35.10</td>
    <td align="right">37.49</td>
    <td align="right">37.59</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.48</td>
    <td align="right">43.56</td>
    <td align="right">43.51</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">19.66</td>
    <td align="right">20.86</td>
    <td align="right">20.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">67.69</td>
    <td align="right">68.96</td>
    <td align="right">68.89</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">67.85</td>
    <td align="right">68.17</td>
    <td align="right">68.17</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">36.27</td>
    <td align="right">37.55</td>
    <td align="right">37.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.70</td>
    <td align="right">88.36</td>
    <td align="right">88.42</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.36</td>
    <td align="right">91.46</td>
    <td align="right">91.44</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">51.58</td>
    <td align="right">51.75</td>
    <td align="right">51.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">9.54</td>
    <td align="right">10.73</td>
    <td align="right">10.75</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">20.08</td>
    <td align="right">19.74</td>
    <td align="right">19.73</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">19.81</td>
    <td align="right">21.15</td>
    <td align="right">21.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">20.25</td>
    <td align="right">22.22</td>
    <td align="right">21.57</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">35.04</td>
    <td align="right">40.49</td>
    <td align="right">40.48</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">38.75</td>
    <td align="right">41.26</td>
    <td align="right">41.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">36.17</td>
    <td align="right">38.52</td>
    <td align="right">38.33</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">68.48</td>
    <td align="right">69.96</td>
    <td align="right">69.91</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">67.94</td>
    <td align="right">69.95</td>
    <td align="right">69.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">51.56</td>
    <td align="right">51.65</td>
    <td align="right">51.61</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.98</td>
    <td align="right">87.34</td>
    <td align="right">87.37</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">95.16</td>
    <td align="right">93.55</td>
    <td align="right">93.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">19.73</td>
    <td align="right">21.28</td>
    <td align="right">24.64</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">49.87</td>
    <td align="right">42.87</td>
    <td align="right">43.30</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">33.25</td>
    <td align="right">33.75</td>
    <td align="right">33.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">41.28</td>
    <td align="right">42.34</td>
    <td align="right">30.91</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">62.68</td>
    <td align="right">57.34</td>
    <td align="right">47.94</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">58.26</td>
    <td align="right">56.26</td>
    <td align="right">56.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">61.21</td>
    <td align="right">63.57</td>
    <td align="right">38.78</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">89.62</td>
    <td align="right">85.37</td>
    <td align="right">62.28</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">85.21</td>
    <td align="right">81.52</td>
    <td align="right">81.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">80.34</td>
    <td align="right">87.33</td>
    <td align="right">54.50</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">108.35</td>
    <td align="right">103.10</td>
    <td align="right">72.68</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">130.98</td>
    <td align="right">116.46</td>
    <td align="right">116.52</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.76</td>
    <td align="right">6.67</td>
    <td align="right">5.58</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">51.71</td>
    <td align="right">45.87</td>
    <td align="right">32.80</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.23</td>
    <td align="right">20.12</td>
    <td align="right">21.43</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">22.94</td>
    <td align="right">23.10</td>
    <td align="right">24.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">77.01</td>
    <td align="right">65.25</td>
    <td align="right">34.50</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">19.70</td>
    <td align="right">20.09</td>
    <td align="right">21.51</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.18</td>
    <td align="right">25.45</td>
    <td align="right">27.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">94.82</td>
    <td align="right">79.86</td>
    <td align="right">33.89</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">23.17</td>
    <td align="right">22.92</td>
    <td align="right">24.20</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">27.41</td>
    <td align="right">26.90</td>
    <td align="right">28.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">123.21</td>
    <td align="right">100.83</td>
    <td align="right">34.59</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">24.31</td>
    <td align="right">24.48</td>
    <td align="right">25.24</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">29.35</td>
    <td align="right">29.08</td>
    <td align="right">29.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">21.24</td>
    <td align="right">38.26</td>
    <td align="right">38.40</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">23.61</td>
    <td align="right">38.07</td>
    <td align="right">38.66</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">16.04</td>
    <td align="right">27.68</td>
    <td align="right">27.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.91</td>
    <td align="right">52.41</td>
    <td align="right">52.43</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">30.28</td>
    <td align="right">52.81</td>
    <td align="right">52.60</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">15.52</td>
    <td align="right">36.99</td>
    <td align="right">26.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">35.70</td>
    <td align="right">72.56</td>
    <td align="right">73.52</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">40.79</td>
    <td align="right">71.95</td>
    <td align="right">72.50</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">25.58</td>
    <td align="right">54.28</td>
    <td align="right">36.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">39.66</td>
    <td align="right">81.78</td>
    <td align="right">82.96</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">46.57</td>
    <td align="right">85.85</td>
    <td align="right">88.60</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">25.82</td>
    <td align="right">54.63</td>
    <td align="right">37.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">16.52</td>
    <td align="right">27.43</td>
    <td align="right">27.41</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">18.51</td>
    <td align="right">30.09</td>
    <td align="right">29.99</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">19.20</td>
    <td align="right">29.81</td>
    <td align="right">29.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">16.54</td>
    <td align="right">44.16</td>
    <td align="right">34.28</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">17.41</td>
    <td align="right">38.37</td>
    <td align="right">28.81</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">19.01</td>
    <td align="right">47.22</td>
    <td align="right">37.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">26.03</td>
    <td align="right">53.83</td>
    <td align="right">36.45</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">30.02</td>
    <td align="right">57.63</td>
    <td align="right">39.57</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">30.89</td>
    <td align="right">57.86</td>
    <td align="right">39.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">26.15</td>
    <td align="right">53.91</td>
    <td align="right">36.80</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">31.19</td>
    <td align="right">59.48</td>
    <td align="right">39.87</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">31.96</td>
    <td align="right">59.22</td>
    <td align="right">39.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">24.54</td>
    <td align="right">41.43</td>
    <td align="right">30.73</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">30.96</td>
    <td align="right">51.57</td>
    <td align="right">33.70</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">34.42</td>
    <td align="right">57.99</td>
    <td align="right">58.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">33.25</td>
    <td align="right">57.15</td>
    <td align="right">31.00</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.10</td>
    <td align="right">58.10</td>
    <td align="right">31.87</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">42.79</td>
    <td align="right">75.46</td>
    <td align="right">78.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">38.33</td>
    <td align="right">70.89</td>
    <td align="right">30.94</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">45.58</td>
    <td align="right">76.49</td>
    <td align="right">33.20</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">46.29</td>
    <td align="right">82.95</td>
    <td align="right">83.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">50.65</td>
    <td align="right">96.41</td>
    <td align="right">32.29</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">55.44</td>
    <td align="right">95.61</td>
    <td align="right">32.93</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">61.89</td>
    <td align="right">112.88</td>
    <td align="right">112.94</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.16</td>
    <td align="right">33.52</td>
    <td align="right">19.65</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">55.86</td>
    <td align="right">48.46</td>
    <td align="right">35.62</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">18.40</td>
    <td align="right">20.40</td>
    <td align="right">22.66</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">23.47</td>
    <td align="right">25.28</td>
    <td align="right">27.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">103.19</td>
    <td align="right">103.75</td>
    <td align="right">45.79</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">21.87</td>
    <td align="right">21.94</td>
    <td align="right">23.42</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">29.07</td>
    <td align="right">29.56</td>
    <td align="right">31.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">214.92</td>
    <td align="right">182.98</td>
    <td align="right">57.16</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">35.68</td>
    <td align="right">35.02</td>
    <td align="right">36.53</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">46.49</td>
    <td align="right">45.18</td>
    <td align="right">46.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">351.10</td>
    <td align="right">292.67</td>
    <td align="right">72.30</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">42.65</td>
    <td align="right">42.40</td>
    <td align="right">43.68</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">58.78</td>
    <td align="right">58.50</td>
    <td align="right">60.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">23.20</td>
    <td align="right">38.85</td>
    <td align="right">38.60</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">25.56</td>
    <td align="right">38.34</td>
    <td align="right">38.79</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">16.28</td>
    <td align="right">29.51</td>
    <td align="right">29.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">31.06</td>
    <td align="right">54.15</td>
    <td align="right">53.99</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">36.50</td>
    <td align="right">54.92</td>
    <td align="right">54.59</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">17.32</td>
    <td align="right">39.91</td>
    <td align="right">29.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">55.77</td>
    <td align="right">86.37</td>
    <td align="right">87.21</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">63.24</td>
    <td align="right">89.31</td>
    <td align="right">89.74</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">45.91</td>
    <td align="right">78.04</td>
    <td align="right">60.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">73.49</td>
    <td align="right">105.06</td>
    <td align="right">105.94</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">83.62</td>
    <td align="right">115.63</td>
    <td align="right">117.65</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">57.54</td>
    <td align="right">91.72</td>
    <td align="right">74.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">17.96</td>
    <td align="right">29.04</td>
    <td align="right">29.05</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">18.73</td>
    <td align="right">31.39</td>
    <td align="right">31.37</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">19.46</td>
    <td align="right">31.00</td>
    <td align="right">30.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">18.59</td>
    <td align="right">48.86</td>
    <td align="right">39.14</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">18.86</td>
    <td align="right">42.03</td>
    <td align="right">32.32</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">21.85</td>
    <td align="right">51.19</td>
    <td align="right">42.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">47.50</td>
    <td align="right">78.23</td>
    <td align="right">62.37</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">50.94</td>
    <td align="right">82.08</td>
    <td align="right">63.82</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">52.22</td>
    <td align="right">81.88</td>
    <td align="right">63.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">59.22</td>
    <td align="right">91.09</td>
    <td align="right">75.49</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">61.40</td>
    <td align="right">96.98</td>
    <td align="right">78.26</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">63.24</td>
    <td align="right">98.13</td>
    <td align="right">78.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">25.91</td>
    <td align="right">41.70</td>
    <td align="right">32.12</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">33.13</td>
    <td align="right">52.73</td>
    <td align="right">36.74</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">36.69</td>
    <td align="right">58.25</td>
    <td align="right">58.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">37.25</td>
    <td align="right">61.04</td>
    <td align="right">35.69</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">45.71</td>
    <td align="right">61.45</td>
    <td align="right">36.04</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">47.91</td>
    <td align="right">81.02</td>
    <td align="right">83.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">56.44</td>
    <td align="right">84.23</td>
    <td align="right">46.00</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">72.64</td>
    <td align="right">99.08</td>
    <td align="right">58.38</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">74.90</td>
    <td align="right">102.73</td>
    <td align="right">103.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">79.97</td>
    <td align="right">118.13</td>
    <td align="right">54.27</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">93.65</td>
    <td align="right">129.13</td>
    <td align="right">70.55</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">107.32</td>
    <td align="right">140.99</td>
    <td align="right">140.94</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->

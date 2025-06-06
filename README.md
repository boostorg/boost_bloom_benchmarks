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
    <td align="right">26.20</td>
    <td align="right">4.41</td>
    <td align="right">3.48</td>
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
    <td align="right">11.04</td>
    <td align="right">10.58</td>
    <td align="right">16.73</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.97</td>
    <td align="right">4.28</td>
    <td align="right">4.28</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.86</td>
    <td align="right">5.08</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.35</td>
    <td align="right">15.45</td>
    <td align="right">17.61</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.81</td>
    <td align="right">4.94</td>
    <td align="right">4.97</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.43</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.07</td>
    <td align="right">18.63</td>
    <td align="right">16.48</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.40</td>
    <td align="right">5.30</td>
    <td align="right">5.36</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.27</td>
    <td align="right">6.31</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.64</td>
    <td align="right">23.03</td>
    <td align="right">16.81</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.18</td>
    <td align="right">5.90</td>
    <td align="right">5.91</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.72</td>
    <td align="right">6.59</td>
    <td align="right">6.60</td>
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
    <td align="right">5.08</td>
    <td align="right">5.73</td>
    <td align="right">5.73</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.25</td>
    <td align="right">6.58</td>
    <td align="right">6.51</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.93</td>
    <td align="right">3.25</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.52</td>
    <td align="right">8.86</td>
    <td align="right">8.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.16</td>
    <td align="right">9.82</td>
    <td align="right">9.84</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.47</td>
    <td align="right">3.12</td>
    <td align="right">3.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.23</td>
    <td align="right">13.17</td>
    <td align="right">13.17</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.68</td>
    <td align="right">15.05</td>
    <td align="right">15.03</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.74</td>
    <td align="right">5.79</td>
    <td align="right">3.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.00</td>
    <td align="right">14.89</td>
    <td align="right">14.84</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.20</td>
    <td align="right">16.18</td>
    <td align="right">16.24</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.75</td>
    <td align="right">5.77</td>
    <td align="right">3.89</td>
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
    <td align="right">2.94</td>
    <td align="right">3.25</td>
    <td align="right">3.22</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.37</td>
    <td align="right">5.10</td>
    <td align="right">5.00</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.55</td>
    <td align="right">4.98</td>
    <td align="right">5.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.04</td>
    <td align="right">3.32</td>
    <td align="right">3.31</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.20</td>
    <td align="right">4.47</td>
    <td align="right">4.47</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.43</td>
    <td align="right">5.11</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.41</td>
    <td align="right">5.49</td>
    <td align="right">3.77</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.00</td>
    <td align="right">7.70</td>
    <td align="right">5.87</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.83</td>
    <td align="right">7.56</td>
    <td align="right">5.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.45</td>
    <td align="right">5.51</td>
    <td align="right">3.80</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.99</td>
    <td align="right">9.12</td>
    <td align="right">6.01</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.32</td>
    <td align="right">9.02</td>
    <td align="right">5.85</td>
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
    <td align="right">6.87</td>
    <td align="right">7.00</td>
    <td align="right">13.59</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.45</td>
    <td align="right">8.97</td>
    <td align="right">17.39</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.67</td>
    <td align="right">10.98</td>
    <td align="right">10.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.37</td>
    <td align="right">8.17</td>
    <td align="right">12.46</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.18</td>
    <td align="right">9.51</td>
    <td align="right">14.32</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">15.73</td>
    <td align="right">15.76</td>
    <td align="right">15.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.98</td>
    <td align="right">10.37</td>
    <td align="right">12.04</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.39</td>
    <td align="right">12.60</td>
    <td align="right">15.24</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">19.23</td>
    <td align="right">19.28</td>
    <td align="right">18.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.48</td>
    <td align="right">12.78</td>
    <td align="right">13.22</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.82</td>
    <td align="right">14.19</td>
    <td align="right">14.91</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">25.71</td>
    <td align="right">26.13</td>
    <td align="right">26.38</td>
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
    <td align="right">31.15</td>
    <td align="right">18.85</td>
    <td align="right">7.01</td>
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
    <td align="right">14.18</td>
    <td align="right">13.19</td>
    <td align="right">17.94</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.82</td>
    <td align="right">5.16</td>
    <td align="right">5.14</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.79</td>
    <td align="right">5.97</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.87</td>
    <td align="right">18.71</td>
    <td align="right">18.47</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.46</td>
    <td align="right">5.58</td>
    <td align="right">5.65</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.23</td>
    <td align="right">6.30</td>
    <td align="right">6.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">25.97</td>
    <td align="right">24.50</td>
    <td align="right">17.64</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.55</td>
    <td align="right">6.29</td>
    <td align="right">6.30</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.44</td>
    <td align="right">7.53</td>
    <td align="right">8.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">40.24</td>
    <td align="right">37.01</td>
    <td align="right">18.61</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">9.80</td>
    <td align="right">8.92</td>
    <td align="right">8.59</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.04</td>
    <td align="right">10.21</td>
    <td align="right">9.63</td>
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
    <td align="right">6.12</td>
    <td align="right">6.93</td>
    <td align="right">6.92</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.30</td>
    <td align="right">7.97</td>
    <td align="right">7.90</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.61</td>
    <td align="right">4.13</td>
    <td align="right">4.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.45</td>
    <td align="right">9.72</td>
    <td align="right">9.82</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.11</td>
    <td align="right">11.07</td>
    <td align="right">11.03</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.59</td>
    <td align="right">5.06</td>
    <td align="right">7.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.99</td>
    <td align="right">14.71</td>
    <td align="right">14.65</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.87</td>
    <td align="right">17.99</td>
    <td align="right">18.13</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.30</td>
    <td align="right">9.24</td>
    <td align="right">4.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.46</td>
    <td align="right">18.50</td>
    <td align="right">23.01</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">21.25</td>
    <td align="right">27.42</td>
    <td align="right">24.08</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.54</td>
    <td align="right">9.18</td>
    <td align="right">6.34</td>
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
    <td align="right">3.63</td>
    <td align="right">4.10</td>
    <td align="right">4.09</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.27</td>
    <td align="right">6.27</td>
    <td align="right">6.11</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.39</td>
    <td align="right">6.05</td>
    <td align="right">6.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.56</td>
    <td align="right">3.98</td>
    <td align="right">3.98</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">4.39</td>
    <td align="right">5.48</td>
    <td align="right">5.22</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">5.12</td>
    <td align="right">6.20</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">11.29</td>
    <td align="right">14.87</td>
    <td align="right">7.21</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.69</td>
    <td align="right">9.97</td>
    <td align="right">7.58</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.60</td>
    <td align="right">10.04</td>
    <td align="right">7.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.98</td>
    <td align="right">8.11</td>
    <td align="right">6.05</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">10.75</td>
    <td align="right">12.60</td>
    <td align="right">8.52</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.26</td>
    <td align="right">12.84</td>
    <td align="right">8.84</td>
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
    <td align="right">8.31</td>
    <td align="right">8.38</td>
    <td align="right">14.20</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.55</td>
    <td align="right">9.40</td>
    <td align="right">17.81</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">14.28</td>
    <td align="right">14.11</td>
    <td align="right">14.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.51</td>
    <td align="right">9.04</td>
    <td align="right">12.81</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.40</td>
    <td align="right">10.55</td>
    <td align="right">14.66</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">22.59</td>
    <td align="right">22.22</td>
    <td align="right">22.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">14.11</td>
    <td align="right">12.71</td>
    <td align="right">13.11</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">17.93</td>
    <td align="right">14.59</td>
    <td align="right">17.23</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">24.90</td>
    <td align="right">24.91</td>
    <td align="right">24.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">19.97</td>
    <td align="right">16.97</td>
    <td align="right">15.01</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">28.87</td>
    <td align="right">20.43</td>
    <td align="right">17.19</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">34.95</td>
    <td align="right">36.16</td>
    <td align="right">35.24</td>
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
    <td align="right">26.51</td>
    <td align="right">4.05</td>
    <td align="right">3.34</td>
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
    <td align="right">9.36</td>
    <td align="right">9.07</td>
    <td align="right">15.33</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.66</td>
    <td align="right">3.95</td>
    <td align="right">4.05</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.89</td>
    <td align="right">4.65</td>
    <td align="right">4.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.18</td>
    <td align="right">13.44</td>
    <td align="right">16.60</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">7.10</td>
    <td align="right">4.56</td>
    <td align="right">4.56</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.49</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.36</td>
    <td align="right">16.64</td>
    <td align="right">15.60</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.49</td>
    <td align="right">5.07</td>
    <td align="right">5.27</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.65</td>
    <td align="right">5.99</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.15</td>
    <td align="right">22.47</td>
    <td align="right">15.82</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.59</td>
    <td align="right">5.69</td>
    <td align="right">5.85</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.86</td>
    <td align="right">3.36</td>
    <td align="right">3.35</td>
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
    <td align="right">3.04</td>
    <td align="right">3.57</td>
    <td align="right">3.57</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.16</td>
    <td align="right">3.53</td>
    <td align="right">3.47</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.59</td>
    <td align="right">2.50</td>
    <td align="right">2.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.72</td>
    <td align="right">4.08</td>
    <td align="right">4.08</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.72</td>
    <td align="right">4.37</td>
    <td align="right">4.41</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.13</td>
    <td align="right">2.26</td>
    <td align="right">2.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.53</td>
    <td align="right">7.09</td>
    <td align="right">7.09</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.80</td>
    <td align="right">7.09</td>
    <td align="right">7.11</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.17</td>
    <td align="right">4.35</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.05</td>
    <td align="right">7.59</td>
    <td align="right">7.62</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.30</td>
    <td align="right">8.05</td>
    <td align="right">8.09</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.23</td>
    <td align="right">4.43</td>
    <td align="right">3.17</td>
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
    <td align="right">2.61</td>
    <td align="right">2.35</td>
    <td align="right">2.35</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.64</td>
    <td align="right">4.05</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.68</td>
    <td align="right">3.93</td>
    <td align="right">3.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.68</td>
    <td align="right">2.46</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.94</td>
    <td align="right">3.73</td>
    <td align="right">3.73</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.85</td>
    <td align="right">4.04</td>
    <td align="right">4.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.25</td>
    <td align="right">4.31</td>
    <td align="right">2.99</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.66</td>
    <td align="right">6.03</td>
    <td align="right">4.63</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.84</td>
    <td align="right">6.04</td>
    <td align="right">4.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.32</td>
    <td align="right">4.35</td>
    <td align="right">2.95</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.59</td>
    <td align="right">7.09</td>
    <td align="right">4.63</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.78</td>
    <td align="right">7.04</td>
    <td align="right">4.57</td>
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
    <td align="right">6.80</td>
    <td align="right">6.08</td>
    <td align="right">12.19</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.37</td>
    <td align="right">7.99</td>
    <td align="right">16.42</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.58</td>
    <td align="right">11.01</td>
    <td align="right">11.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.41</td>
    <td align="right">8.17</td>
    <td align="right">12.17</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.16</td>
    <td align="right">9.54</td>
    <td align="right">13.89</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.88</td>
    <td align="right">15.51</td>
    <td align="right">15.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.63</td>
    <td align="right">9.95</td>
    <td align="right">11.80</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.43</td>
    <td align="right">12.38</td>
    <td align="right">14.75</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.97</td>
    <td align="right">17.09</td>
    <td align="right">17.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.85</td>
    <td align="right">12.31</td>
    <td align="right">12.51</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">18.07</td>
    <td align="right">13.93</td>
    <td align="right">14.32</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">22.12</td>
    <td align="right">22.23</td>
    <td align="right">21.52</td>
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
    <td align="right">33.57</td>
    <td align="right">16.99</td>
    <td align="right">6.98</td>
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
    <td align="right">10.78</td>
    <td align="right">10.44</td>
    <td align="right">16.04</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.54</td>
    <td align="right">4.39</td>
    <td align="right">4.52</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.55</td>
    <td align="right">4.95</td>
    <td align="right">4.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.00</td>
    <td align="right">15.93</td>
    <td align="right">17.48</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.79</td>
    <td align="right">6.84</td>
    <td align="right">5.05</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.06</td>
    <td align="right">6.32</td>
    <td align="right">5.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">30.97</td>
    <td align="right">38.56</td>
    <td align="right">17.78</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.00</td>
    <td align="right">9.00</td>
    <td align="right">10.28</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">12.38</td>
    <td align="right">9.28</td>
    <td align="right">9.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">48.12</td>
    <td align="right">48.81</td>
    <td align="right">19.31</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.38</td>
    <td align="right">17.70</td>
    <td align="right">18.37</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.46</td>
    <td align="right">8.24</td>
    <td align="right">7.79</td>
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
    <td align="right">3.47</td>
    <td align="right">4.01</td>
    <td align="right">4.09</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.56</td>
    <td align="right">3.93</td>
    <td align="right">3.90</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.97</td>
    <td align="right">2.95</td>
    <td align="right">2.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.39</td>
    <td align="right">4.84</td>
    <td align="right">4.96</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.18</td>
    <td align="right">5.62</td>
    <td align="right">5.16</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.50</td>
    <td align="right">2.67</td>
    <td align="right">2.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">6.81</td>
    <td align="right">9.06</td>
    <td align="right">8.52</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.45</td>
    <td align="right">9.16</td>
    <td align="right">9.49</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.07</td>
    <td align="right">7.82</td>
    <td align="right">4.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">9.92</td>
    <td align="right">13.31</td>
    <td align="right">17.26</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">11.69</td>
    <td align="right">18.88</td>
    <td align="right">15.60</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">11.62</td>
    <td align="right">12.99</td>
    <td align="right">8.95</td>
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
    <td align="right">2.94</td>
    <td align="right">2.72</td>
    <td align="right">2.70</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.10</td>
    <td align="right">4.55</td>
    <td align="right">4.57</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.10</td>
    <td align="right">4.38</td>
    <td align="right">4.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.94</td>
    <td align="right">2.70</td>
    <td align="right">2.67</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.24</td>
    <td align="right">4.13</td>
    <td align="right">4.06</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.12</td>
    <td align="right">4.31</td>
    <td align="right">4.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.67</td>
    <td align="right">8.72</td>
    <td align="right">4.78</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">7.61</td>
    <td align="right">9.08</td>
    <td align="right">6.35</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">7.12</td>
    <td align="right">7.22</td>
    <td align="right">5.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.57</td>
    <td align="right">11.72</td>
    <td align="right">4.49</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">9.06</td>
    <td align="right">9.00</td>
    <td align="right">6.12</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">8.81</td>
    <td align="right">8.93</td>
    <td align="right">6.08</td>
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
    <td align="right">7.58</td>
    <td align="right">6.69</td>
    <td align="right">12.42</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">11.73</td>
    <td align="right">8.65</td>
    <td align="right">16.79</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">12.85</td>
    <td align="right">13.17</td>
    <td align="right">13.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">9.91</td>
    <td align="right">8.48</td>
    <td align="right">12.22</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">12.46</td>
    <td align="right">9.86</td>
    <td align="right">14.02</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">17.56</td>
    <td align="right">17.67</td>
    <td align="right">17.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">12.81</td>
    <td align="right">11.22</td>
    <td align="right">16.04</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">31.14</td>
    <td align="right">21.44</td>
    <td align="right">16.39</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">23.99</td>
    <td align="right">23.27</td>
    <td align="right">20.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">20.93</td>
    <td align="right">34.15</td>
    <td align="right">19.57</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">35.77</td>
    <td align="right">20.63</td>
    <td align="right">16.13</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">31.01</td>
    <td align="right">31.58</td>
    <td align="right">31.89</td>
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
    <td align="right">27.10</td>
    <td align="right">6.70</td>
    <td align="right">4.62</td>
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
    <td align="right">9.39</td>
    <td align="right">7.53</td>
    <td align="right">18.74</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.90</td>
    <td align="right">1.39</td>
    <td align="right">1.66</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.22</td>
    <td align="right">2.22</td>
    <td align="right">2.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.07</td>
    <td align="right">10.06</td>
    <td align="right">25.22</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">2.46</td>
    <td align="right">2.48</td>
    <td align="right">2.50</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">2.70</td>
    <td align="right">2.55</td>
    <td align="right">2.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">22.05</td>
    <td align="right">15.23</td>
    <td align="right">21.16</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">3.05</td>
    <td align="right">2.93</td>
    <td align="right">2.82</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.94</td>
    <td align="right">2.66</td>
    <td align="right">3.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">47.72</td>
    <td align="right">22.13</td>
    <td align="right">22.66</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.53</td>
    <td align="right">4.07</td>
    <td align="right">2.86</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">3.95</td>
    <td align="right">2.76</td>
    <td align="right">3.56</td>
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
    <td align="right">4.02</td>
    <td align="right">2.99</td>
    <td align="right">3.02</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.83</td>
    <td align="right">2.72</td>
    <td align="right">3.51</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.47</td>
    <td align="right">3.14</td>
    <td align="right">2.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.69</td>
    <td align="right">3.56</td>
    <td align="right">5.17</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.62</td>
    <td align="right">3.78</td>
    <td align="right">4.04</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">3.06</td>
    <td align="right">2.95</td>
    <td align="right">2.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">6.96</td>
    <td align="right">5.89</td>
    <td align="right">4.09</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">8.71</td>
    <td align="right">6.22</td>
    <td align="right">7.03</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.71</td>
    <td align="right">5.31</td>
    <td align="right">3.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">8.02</td>
    <td align="right">6.15</td>
    <td align="right">6.28</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">10.63</td>
    <td align="right">6.79</td>
    <td align="right">8.08</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.60</td>
    <td align="right">6.32</td>
    <td align="right">2.97</td>
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
    <td align="right">3.06</td>
    <td align="right">3.50</td>
    <td align="right">3.56</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.58</td>
    <td align="right">2.72</td>
    <td align="right">2.35</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.86</td>
    <td align="right">2.52</td>
    <td align="right">2.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.21</td>
    <td align="right">3.11</td>
    <td align="right">2.76</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.80</td>
    <td align="right">3.36</td>
    <td align="right">3.25</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.79</td>
    <td align="right">3.19</td>
    <td align="right">3.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.74</td>
    <td align="right">4.50</td>
    <td align="right">2.93</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">6.79</td>
    <td align="right">6.76</td>
    <td align="right">10.25</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.61</td>
    <td align="right">7.34</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.71</td>
    <td align="right">5.76</td>
    <td align="right">3.33</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">10.01</td>
    <td align="right">6.99</td>
    <td align="right">6.61</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">8.73</td>
    <td align="right">6.42</td>
    <td align="right">5.81</td>
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
    <td align="right">5.93</td>
    <td align="right">5.74</td>
    <td align="right">13.67</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">10.90</td>
    <td align="right">5.99</td>
    <td align="right">19.51</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">11.77</td>
    <td align="right">7.31</td>
    <td align="right">9.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.56</td>
    <td align="right">7.13</td>
    <td align="right">17.40</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.97</td>
    <td align="right">6.34</td>
    <td align="right">13.14</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">13.91</td>
    <td align="right">9.50</td>
    <td align="right">9.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">8.94</td>
    <td align="right">7.67</td>
    <td align="right">12.22</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">16.55</td>
    <td align="right">10.31</td>
    <td align="right">20.19</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">17.05</td>
    <td align="right">12.57</td>
    <td align="right">10.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">15.17</td>
    <td align="right">15.26</td>
    <td align="right">15.50</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">16.81</td>
    <td align="right">19.78</td>
    <td align="right">21.19</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">32.85</td>
    <td align="right">15.21</td>
    <td align="right">19.02</td>
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
    <td align="right">35.77</td>
    <td align="right">17.03</td>
    <td align="right">12.69</td>
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
    <td align="right">13.13</td>
    <td align="right">12.42</td>
    <td align="right">19.49</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.39</td>
    <td align="right">3.72</td>
    <td align="right">6.26</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.65</td>
    <td align="right">4.27</td>
    <td align="right">3.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">30.98</td>
    <td align="right">26.10</td>
    <td align="right">24.87</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">7.78</td>
    <td align="right">7.48</td>
    <td align="right">7.54</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.56</td>
    <td align="right">5.67</td>
    <td align="right">5.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">69.89</td>
    <td align="right">63.55</td>
    <td align="right">32.22</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">11.10</td>
    <td align="right">13.31</td>
    <td align="right">10.17</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.73</td>
    <td align="right">13.92</td>
    <td align="right">12.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">93.27</td>
    <td align="right">67.22</td>
    <td align="right">35.60</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.91</td>
    <td align="right">15.64</td>
    <td align="right">11.93</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">11.45</td>
    <td align="right">9.34</td>
    <td align="right">10.80</td>
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
    <td align="right">4.16</td>
    <td align="right">4.94</td>
    <td align="right">3.79</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.92</td>
    <td align="right">5.08</td>
    <td align="right">4.31</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.84</td>
    <td align="right">3.88</td>
    <td align="right">6.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.52</td>
    <td align="right">10.30</td>
    <td align="right">8.38</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.25</td>
    <td align="right">8.35</td>
    <td align="right">9.40</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.86</td>
    <td align="right">5.84</td>
    <td align="right">8.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.64</td>
    <td align="right">16.39</td>
    <td align="right">16.35</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.80</td>
    <td align="right">15.88</td>
    <td align="right">16.29</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">12.61</td>
    <td align="right">13.05</td>
    <td align="right">7.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.14</td>
    <td align="right">13.47</td>
    <td align="right">13.02</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.80</td>
    <td align="right">15.81</td>
    <td align="right">14.30</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.84</td>
    <td align="right">10.90</td>
    <td align="right">6.47</td>
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
    <td align="right">2.41</td>
    <td align="right">2.59</td>
    <td align="right">2.57</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.89</td>
    <td align="right">2.61</td>
    <td align="right">2.60</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.74</td>
    <td align="right">2.65</td>
    <td align="right">2.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.91</td>
    <td align="right">3.26</td>
    <td align="right">3.07</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.93</td>
    <td align="right">4.92</td>
    <td align="right">5.07</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">5.28</td>
    <td align="right">5.88</td>
    <td align="right">5.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">8.01</td>
    <td align="right">7.89</td>
    <td align="right">5.02</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.58</td>
    <td align="right">11.90</td>
    <td align="right">13.21</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.94</td>
    <td align="right">10.20</td>
    <td align="right">9.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.67</td>
    <td align="right">11.35</td>
    <td align="right">7.21</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.64</td>
    <td align="right">14.23</td>
    <td align="right">13.61</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.22</td>
    <td align="right">14.61</td>
    <td align="right">16.65</td>
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
    <td align="right">4.87</td>
    <td align="right">4.26</td>
    <td align="right">11.90</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">10.50</td>
    <td align="right">5.06</td>
    <td align="right">15.14</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">10.79</td>
    <td align="right">8.23</td>
    <td align="right">7.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">14.01</td>
    <td align="right">11.55</td>
    <td align="right">16.96</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">21.49</td>
    <td align="right">13.42</td>
    <td align="right">19.17</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">22.03</td>
    <td align="right">25.68</td>
    <td align="right">25.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">24.30</td>
    <td align="right">16.09</td>
    <td align="right">16.52</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">46.54</td>
    <td align="right">24.02</td>
    <td align="right">22.22</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">43.40</td>
    <td align="right">38.34</td>
    <td align="right">38.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">33.74</td>
    <td align="right">26.82</td>
    <td align="right">17.90</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">51.08</td>
    <td align="right">36.72</td>
    <td align="right">22.60</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">67.43</td>
    <td align="right">57.75</td>
    <td align="right">56.72</td>
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
    <td align="right">36.39</td>
    <td align="right">5.92</td>
    <td align="right">3.72</td>
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
    <td align="right">12.08</td>
    <td align="right">12.56</td>
    <td align="right">16.99</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.89</td>
    <td align="right">4.42</td>
    <td align="right">4.20</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.93</td>
    <td align="right">5.22</td>
    <td align="right">5.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.51</td>
    <td align="right">17.78</td>
    <td align="right">17.64</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.93</td>
    <td align="right">4.83</td>
    <td align="right">4.73</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.06</td>
    <td align="right">5.93</td>
    <td align="right">5.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.84</td>
    <td align="right">21.36</td>
    <td align="right">16.64</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.61</td>
    <td align="right">5.52</td>
    <td align="right">5.32</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.29</td>
    <td align="right">6.57</td>
    <td align="right">6.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.00</td>
    <td align="right">26.92</td>
    <td align="right">17.53</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.92</td>
    <td align="right">5.88</td>
    <td align="right">5.88</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.37</td>
    <td align="right">7.39</td>
    <td align="right">7.45</td>
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
    <td align="right">7.84</td>
    <td align="right">5.49</td>
    <td align="right">5.50</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.16</td>
    <td align="right">5.60</td>
    <td align="right">5.56</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.34</td>
    <td align="right">3.89</td>
    <td align="right">3.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.58</td>
    <td align="right">8.09</td>
    <td align="right">8.18</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.39</td>
    <td align="right">8.65</td>
    <td align="right">7.79</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.87</td>
    <td align="right">4.82</td>
    <td align="right">4.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.10</td>
    <td align="right">10.91</td>
    <td align="right">10.72</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">23.56</td>
    <td align="right">10.48</td>
    <td align="right">10.88</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.04</td>
    <td align="right">7.10</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">16.97</td>
    <td align="right">12.55</td>
    <td align="right">12.45</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">22.58</td>
    <td align="right">13.59</td>
    <td align="right">13.80</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.13</td>
    <td align="right">7.00</td>
    <td align="right">5.39</td>
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
    <td align="right">3.26</td>
    <td align="right">3.82</td>
    <td align="right">3.86</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.47</td>
    <td align="right">5.50</td>
    <td align="right">5.49</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.63</td>
    <td align="right">5.38</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.34</td>
    <td align="right">5.50</td>
    <td align="right">4.65</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.83</td>
    <td align="right">5.76</td>
    <td align="right">4.95</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.94</td>
    <td align="right">7.03</td>
    <td align="right">6.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.08</td>
    <td align="right">6.76</td>
    <td align="right">5.04</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.79</td>
    <td align="right">9.26</td>
    <td align="right">7.58</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.68</td>
    <td align="right">9.24</td>
    <td align="right">7.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.12</td>
    <td align="right">6.82</td>
    <td align="right">5.08</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.11</td>
    <td align="right">10.74</td>
    <td align="right">7.67</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.15</td>
    <td align="right">10.48</td>
    <td align="right">7.48</td>
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
    <td align="right">8.54</td>
    <td align="right">8.56</td>
    <td align="right">13.67</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.05</td>
    <td align="right">11.61</td>
    <td align="right">17.05</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">12.78</td>
    <td align="right">10.46</td>
    <td align="right">10.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.74</td>
    <td align="right">10.91</td>
    <td align="right">12.99</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.29</td>
    <td align="right">12.90</td>
    <td align="right">14.44</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">16.97</td>
    <td align="right">15.59</td>
    <td align="right">15.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.29</td>
    <td align="right">14.07</td>
    <td align="right">12.67</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">19.09</td>
    <td align="right">17.32</td>
    <td align="right">15.27</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">21.39</td>
    <td align="right">17.83</td>
    <td align="right">17.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.66</td>
    <td align="right">17.38</td>
    <td align="right">13.97</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">20.53</td>
    <td align="right">20.31</td>
    <td align="right">14.92</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">28.67</td>
    <td align="right">25.45</td>
    <td align="right">25.65</td>
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
    <td align="right">46.00</td>
    <td align="right">22.69</td>
    <td align="right">10.78</td>
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
    <td align="right">14.57</td>
    <td align="right">13.31</td>
    <td align="right">17.84</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.11</td>
    <td align="right">4.48</td>
    <td align="right">4.67</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.99</td>
    <td align="right">5.80</td>
    <td align="right">5.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">26.33</td>
    <td align="right">24.33</td>
    <td align="right">19.60</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.05</td>
    <td align="right">8.60</td>
    <td align="right">6.88</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">13.25</td>
    <td align="right">9.05</td>
    <td align="right">8.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">46.53</td>
    <td align="right">46.94</td>
    <td align="right">21.01</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">17.92</td>
    <td align="right">12.79</td>
    <td align="right">13.01</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">22.46</td>
    <td align="right">19.06</td>
    <td align="right">16.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">89.04</td>
    <td align="right">78.16</td>
    <td align="right">22.55</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.27</td>
    <td align="right">11.04</td>
    <td align="right">12.93</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">21.69</td>
    <td align="right">17.03</td>
    <td align="right">16.50</td>
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
    <td align="right">9.23</td>
    <td align="right">6.21</td>
    <td align="right">6.19</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">11.98</td>
    <td align="right">6.26</td>
    <td align="right">6.23</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.75</td>
    <td align="right">4.20</td>
    <td align="right">4.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.14</td>
    <td align="right">9.66</td>
    <td align="right">9.59</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.29</td>
    <td align="right">9.32</td>
    <td align="right">8.79</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.60</td>
    <td align="right">5.98</td>
    <td align="right">4.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.38</td>
    <td align="right">14.82</td>
    <td align="right">13.71</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">27.56</td>
    <td align="right">14.01</td>
    <td align="right">12.38</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.94</td>
    <td align="right">9.52</td>
    <td align="right">6.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">27.57</td>
    <td align="right">21.69</td>
    <td align="right">24.11</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">34.82</td>
    <td align="right">23.24</td>
    <td align="right">25.08</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">12.42</td>
    <td align="right">14.40</td>
    <td align="right">10.94</td>
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
    <td align="right">3.55</td>
    <td align="right">4.07</td>
    <td align="right">4.09</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.92</td>
    <td align="right">5.85</td>
    <td align="right">5.84</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.11</td>
    <td align="right">5.74</td>
    <td align="right">5.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.80</td>
    <td align="right">6.12</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.75</td>
    <td align="right">6.35</td>
    <td align="right">5.55</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.59</td>
    <td align="right">7.71</td>
    <td align="right">6.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.94</td>
    <td align="right">10.05</td>
    <td align="right">7.55</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">12.95</td>
    <td align="right">10.81</td>
    <td align="right">8.78</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">10.84</td>
    <td align="right">10.35</td>
    <td align="right">8.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.90</td>
    <td align="right">16.49</td>
    <td align="right">10.53</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">15.34</td>
    <td align="right">16.73</td>
    <td align="right">11.90</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.84</td>
    <td align="right">17.72</td>
    <td align="right">14.43</td>
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
    <td align="right">9.64</td>
    <td align="right">9.52</td>
    <td align="right">13.94</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.61</td>
    <td align="right">12.56</td>
    <td align="right">17.73</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">15.16</td>
    <td align="right">13.50</td>
    <td align="right">13.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">14.26</td>
    <td align="right">12.69</td>
    <td align="right">13.67</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">17.78</td>
    <td align="right">22.67</td>
    <td align="right">16.75</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">21.15</td>
    <td align="right">19.08</td>
    <td align="right">19.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">23.02</td>
    <td align="right">25.06</td>
    <td align="right">16.97</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">39.49</td>
    <td align="right">32.52</td>
    <td align="right">19.66</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">27.74</td>
    <td align="right">27.38</td>
    <td align="right">26.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">40.82</td>
    <td align="right">38.28</td>
    <td align="right">20.28</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">49.14</td>
    <td align="right">49.24</td>
    <td align="right">21.78</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">46.51</td>
    <td align="right">37.61</td>
    <td align="right">36.06</td>
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
    <td align="right">62.33</td>
    <td align="right">33.20</td>
    <td align="right">18.14</td>
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
    <td align="right">28.02</td>
    <td align="right">42.35</td>
    <td align="right">36.20</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.52</td>
    <td align="right">15.60</td>
    <td align="right">15.59</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.23</td>
    <td align="right">19.22</td>
    <td align="right">19.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.98</td>
    <td align="right">63.60</td>
    <td align="right">39.85</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.33</td>
    <td align="right">19.63</td>
    <td align="right">19.64</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.27</td>
    <td align="right">18.69</td>
    <td align="right">18.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">45.08</td>
    <td align="right">77.78</td>
    <td align="right">38.43</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.40</td>
    <td align="right">18.47</td>
    <td align="right">18.57</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.06</td>
    <td align="right">18.30</td>
    <td align="right">18.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">53.79</td>
    <td align="right">91.21</td>
    <td align="right">35.26</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">17.47</td>
    <td align="right">18.68</td>
    <td align="right">18.66</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.19</td>
    <td align="right">19.59</td>
    <td align="right">19.58</td>
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
    <td align="right">16.21</td>
    <td align="right">21.25</td>
    <td align="right">21.31</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.77</td>
    <td align="right">22.37</td>
    <td align="right">22.39</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">11.14</td>
    <td align="right">13.64</td>
    <td align="right">13.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.37</td>
    <td align="right">25.99</td>
    <td align="right">25.97</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.75</td>
    <td align="right">27.99</td>
    <td align="right">27.98</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">13.04</td>
    <td align="right">16.36</td>
    <td align="right">16.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.47</td>
    <td align="right">33.63</td>
    <td align="right">33.65</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.88</td>
    <td align="right">46.79</td>
    <td align="right">47.05</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">15.05</td>
    <td align="right">19.57</td>
    <td align="right">19.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">33.23</td>
    <td align="right">34.48</td>
    <td align="right">34.35</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">76.49</td>
    <td align="right">55.46</td>
    <td align="right">55.47</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">21.64</td>
    <td align="right">23.98</td>
    <td align="right">24.00</td>
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
    <td align="right">15.40</td>
    <td align="right">15.65</td>
    <td align="right">15.63</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.25</td>
    <td align="right">21.28</td>
    <td align="right">21.30</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.73</td>
    <td align="right">22.35</td>
    <td align="right">22.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.98</td>
    <td align="right">20.52</td>
    <td align="right">20.46</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.43</td>
    <td align="right">26.01</td>
    <td align="right">26.01</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">40.52</td>
    <td align="right">27.92</td>
    <td align="right">27.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.84</td>
    <td align="right">24.90</td>
    <td align="right">24.93</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.07</td>
    <td align="right">33.42</td>
    <td align="right">33.40</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.81</td>
    <td align="right">46.74</td>
    <td align="right">47.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">33.64</td>
    <td align="right">35.48</td>
    <td align="right">35.34</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">33.12</td>
    <td align="right">34.05</td>
    <td align="right">34.08</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">76.36</td>
    <td align="right">55.46</td>
    <td align="right">55.48</td>
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
    <td align="right">17.26</td>
    <td align="right">20.76</td>
    <td align="right">25.55</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.36</td>
    <td align="right">29.33</td>
    <td align="right">34.68</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">27.81</td>
    <td align="right">30.16</td>
    <td align="right">30.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.18</td>
    <td align="right">28.40</td>
    <td align="right">26.37</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">39.05</td>
    <td align="right">33.53</td>
    <td align="right">30.62</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">38.13</td>
    <td align="right">38.62</td>
    <td align="right">39.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.68</td>
    <td align="right">33.72</td>
    <td align="right">25.71</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">47.13</td>
    <td align="right">41.80</td>
    <td align="right">33.52</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">39.85</td>
    <td align="right">41.71</td>
    <td align="right">42.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">36.21</td>
    <td align="right">38.26</td>
    <td align="right">25.88</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">47.09</td>
    <td align="right">42.12</td>
    <td align="right">30.13</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">54.17</td>
    <td align="right">58.72</td>
    <td align="right">58.70</td>
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
    <td align="right">81.82</td>
    <td align="right">112.25</td>
    <td align="right">21.70</td>
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
    <td align="right">27.91</td>
    <td align="right">43.29</td>
    <td align="right">39.51</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.81</td>
    <td align="right">15.64</td>
    <td align="right">15.60</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">17.02</td>
    <td align="right">19.69</td>
    <td align="right">19.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">40.51</td>
    <td align="right">64.41</td>
    <td align="right">44.55</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">19.00</td>
    <td align="right">23.12</td>
    <td align="right">22.51</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">17.36</td>
    <td align="right">19.88</td>
    <td align="right">19.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">49.22</td>
    <td align="right">82.36</td>
    <td align="right">41.59</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">18.35</td>
    <td align="right">21.11</td>
    <td align="right">21.38</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">19.06</td>
    <td align="right">21.11</td>
    <td align="right">22.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">85.50</td>
    <td align="right">136.96</td>
    <td align="right">45.94</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">24.06</td>
    <td align="right">23.69</td>
    <td align="right">27.37</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">25.07</td>
    <td align="right">38.50</td>
    <td align="right">34.03</td>
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
    <td align="right">16.61</td>
    <td align="right">22.00</td>
    <td align="right">21.88</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.68</td>
    <td align="right">23.13</td>
    <td align="right">23.65</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.15</td>
    <td align="right">13.92</td>
    <td align="right">14.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">28.46</td>
    <td align="right">34.19</td>
    <td align="right">41.46</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">73.43</td>
    <td align="right">45.67</td>
    <td align="right">46.05</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">15.67</td>
    <td align="right">17.85</td>
    <td align="right">18.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">51.97</td>
    <td align="right">62.66</td>
    <td align="right">60.87</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">99.74</td>
    <td align="right">83.35</td>
    <td align="right">88.58</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">30.17</td>
    <td align="right">30.26</td>
    <td align="right">40.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">54.94</td>
    <td align="right">45.83</td>
    <td align="right">54.40</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">97.04</td>
    <td align="right">68.77</td>
    <td align="right">69.49</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">42.43</td>
    <td align="right">36.12</td>
    <td align="right">53.27</td>
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
    <td align="right">17.49</td>
    <td align="right">16.96</td>
    <td align="right">17.52</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">17.10</td>
    <td align="right">22.12</td>
    <td align="right">22.38</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">36.49</td>
    <td align="right">24.14</td>
    <td align="right">24.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">23.75</td>
    <td align="right">28.93</td>
    <td align="right">24.09</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">22.81</td>
    <td align="right">27.18</td>
    <td align="right">26.76</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">60.19</td>
    <td align="right">50.77</td>
    <td align="right">33.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">38.65</td>
    <td align="right">41.05</td>
    <td align="right">52.15</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">58.15</td>
    <td align="right">75.97</td>
    <td align="right">82.58</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">91.28</td>
    <td align="right">69.92</td>
    <td align="right">80.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">102.33</td>
    <td align="right">93.39</td>
    <td align="right">88.61</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">64.52</td>
    <td align="right">65.56</td>
    <td align="right">79.06</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">115.01</td>
    <td align="right">83.32</td>
    <td align="right">77.47</td>
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
    <td align="right">17.84</td>
    <td align="right">21.72</td>
    <td align="right">28.63</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">37.31</td>
    <td align="right">29.77</td>
    <td align="right">36.29</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">29.39</td>
    <td align="right">32.53</td>
    <td align="right">32.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">31.62</td>
    <td align="right">33.35</td>
    <td align="right">42.99</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">66.50</td>
    <td align="right">80.06</td>
    <td align="right">41.39</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">39.84</td>
    <td align="right">41.56</td>
    <td align="right">41.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">62.49</td>
    <td align="right">64.22</td>
    <td align="right">37.07</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">89.21</td>
    <td align="right">82.40</td>
    <td align="right">61.73</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">62.06</td>
    <td align="right">54.28</td>
    <td align="right">53.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">107.40</td>
    <td align="right">99.93</td>
    <td align="right">45.51</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">111.58</td>
    <td align="right">113.08</td>
    <td align="right">66.79</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">96.33</td>
    <td align="right">98.46</td>
    <td align="right">104.91</td>
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
    <td align="right">60.62</td>
    <td align="right">10.47</td>
    <td align="right">7.44</td>
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
    <td align="right">13.79</td>
    <td align="right">22.70</td>
    <td align="right">26.63</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">10.34</td>
    <td align="right">12.39</td>
    <td align="right">12.44</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">28.71</td>
    <td align="right">13.86</td>
    <td align="right">13.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.87</td>
    <td align="right">35.55</td>
    <td align="right">29.20</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">31.15</td>
    <td align="right">14.07</td>
    <td align="right">14.08</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">14.73</td>
    <td align="right">15.36</td>
    <td align="right">15.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.12</td>
    <td align="right">47.74</td>
    <td align="right">29.45</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">14.75</td>
    <td align="right">15.42</td>
    <td align="right">15.42</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">16.32</td>
    <td align="right">16.78</td>
    <td align="right">16.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">29.87</td>
    <td align="right">59.99</td>
    <td align="right">29.62</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">15.38</td>
    <td align="right">15.44</td>
    <td align="right">15.44</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">16.45</td>
    <td align="right">17.02</td>
    <td align="right">17.00</td>
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
    <td align="right">12.71</td>
    <td align="right">16.12</td>
    <td align="right">16.15</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.34</td>
    <td align="right">16.74</td>
    <td align="right">16.71</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.03</td>
    <td align="right">9.39</td>
    <td align="right">9.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.37</td>
    <td align="right">22.41</td>
    <td align="right">22.45</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.85</td>
    <td align="right">22.28</td>
    <td align="right">22.24</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.09</td>
    <td align="right">14.18</td>
    <td align="right">14.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.08</td>
    <td align="right">32.22</td>
    <td align="right">32.21</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.80</td>
    <td align="right">31.00</td>
    <td align="right">30.97</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.75</td>
    <td align="right">17.59</td>
    <td align="right">17.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">25.96</td>
    <td align="right">34.06</td>
    <td align="right">34.13</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.10</td>
    <td align="right">33.94</td>
    <td align="right">34.23</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">15.20</td>
    <td align="right">18.91</td>
    <td align="right">18.89</td>
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
    <td align="right">6.59</td>
    <td align="right">9.42</td>
    <td align="right">9.40</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.71</td>
    <td align="right">16.14</td>
    <td align="right">16.15</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.28</td>
    <td align="right">16.73</td>
    <td align="right">16.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">11.36</td>
    <td align="right">13.72</td>
    <td align="right">13.73</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.42</td>
    <td align="right">22.45</td>
    <td align="right">22.48</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.84</td>
    <td align="right">22.25</td>
    <td align="right">22.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.14</td>
    <td align="right">17.65</td>
    <td align="right">17.66</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.12</td>
    <td align="right">32.19</td>
    <td align="right">32.17</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.80</td>
    <td align="right">30.98</td>
    <td align="right">30.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">15.18</td>
    <td align="right">19.24</td>
    <td align="right">19.23</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">25.92</td>
    <td align="right">34.04</td>
    <td align="right">34.09</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">31.95</td>
    <td align="right">33.95</td>
    <td align="right">33.92</td>
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
    <td align="right">13.48</td>
    <td align="right">16.21</td>
    <td align="right">19.94</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">48.58</td>
    <td align="right">34.03</td>
    <td align="right">37.50</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">20.82</td>
    <td align="right">24.37</td>
    <td align="right">24.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.80</td>
    <td align="right">23.43</td>
    <td align="right">20.71</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">54.31</td>
    <td align="right">37.72</td>
    <td align="right">36.09</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">27.37</td>
    <td align="right">31.99</td>
    <td align="right">32.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.07</td>
    <td align="right">30.07</td>
    <td align="right">20.53</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">60.18</td>
    <td align="right">45.89</td>
    <td align="right">37.14</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">30.82</td>
    <td align="right">35.87</td>
    <td align="right">35.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">28.50</td>
    <td align="right">33.74</td>
    <td align="right">20.64</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">66.76</td>
    <td align="right">48.62</td>
    <td align="right">37.78</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">41.49</td>
    <td align="right">44.85</td>
    <td align="right">45.05</td>
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
    <td align="right">81.85</td>
    <td align="right">48.32</td>
    <td align="right">11.13</td>
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
    <td align="right">14.21</td>
    <td align="right">23.15</td>
    <td align="right">28.44</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">10.56</td>
    <td align="right">12.58</td>
    <td align="right">12.69</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">29.55</td>
    <td align="right">14.03</td>
    <td align="right">14.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.34</td>
    <td align="right">34.71</td>
    <td align="right">29.75</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">31.50</td>
    <td align="right">14.04</td>
    <td align="right">14.01</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">14.60</td>
    <td align="right">15.10</td>
    <td align="right">15.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">25.57</td>
    <td align="right">49.53</td>
    <td align="right">30.25</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">16.79</td>
    <td align="right">15.66</td>
    <td align="right">16.25</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">16.64</td>
    <td align="right">19.26</td>
    <td align="right">17.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">38.73</td>
    <td align="right">76.94</td>
    <td align="right">34.36</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">21.77</td>
    <td align="right">22.01</td>
    <td align="right">20.78</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">23.10</td>
    <td align="right">23.59</td>
    <td align="right">22.79</td>
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
    <td align="right">12.80</td>
    <td align="right">16.67</td>
    <td align="right">16.66</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.35</td>
    <td align="right">17.51</td>
    <td align="right">17.60</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.20</td>
    <td align="right">9.47</td>
    <td align="right">9.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.00</td>
    <td align="right">21.67</td>
    <td align="right">21.89</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.52</td>
    <td align="right">22.45</td>
    <td align="right">21.96</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.44</td>
    <td align="right">14.13</td>
    <td align="right">13.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">26.09</td>
    <td align="right">35.50</td>
    <td align="right">36.76</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">29.65</td>
    <td align="right">33.20</td>
    <td align="right">33.25</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">13.56</td>
    <td align="right">18.37</td>
    <td align="right">20.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">32.56</td>
    <td align="right">45.29</td>
    <td align="right">45.69</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">39.05</td>
    <td align="right">44.50</td>
    <td align="right">42.08</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">22.68</td>
    <td align="right">35.07</td>
    <td align="right">29.87</td>
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
    <td align="right">6.75</td>
    <td align="right">9.74</td>
    <td align="right">9.57</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.87</td>
    <td align="right">16.71</td>
    <td align="right">16.79</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.37</td>
    <td align="right">17.54</td>
    <td align="right">17.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.85</td>
    <td align="right">13.50</td>
    <td align="right">13.47</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.85</td>
    <td align="right">22.12</td>
    <td align="right">22.11</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">17.95</td>
    <td align="right">21.95</td>
    <td align="right">21.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">13.52</td>
    <td align="right">21.89</td>
    <td align="right">17.80</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">25.23</td>
    <td align="right">34.87</td>
    <td align="right">35.99</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">27.23</td>
    <td align="right">32.87</td>
    <td align="right">33.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">22.91</td>
    <td align="right">28.80</td>
    <td align="right">29.93</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">32.85</td>
    <td align="right">45.69</td>
    <td align="right">45.78</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">40.50</td>
    <td align="right">46.20</td>
    <td align="right">43.16</td>
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
    <td align="right">13.54</td>
    <td align="right">16.59</td>
    <td align="right">20.33</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">49.08</td>
    <td align="right">33.07</td>
    <td align="right">36.50</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">22.02</td>
    <td align="right">26.06</td>
    <td align="right">25.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">20.06</td>
    <td align="right">23.71</td>
    <td align="right">20.74</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">58.05</td>
    <td align="right">37.30</td>
    <td align="right">35.73</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">29.21</td>
    <td align="right">33.35</td>
    <td align="right">33.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.38</td>
    <td align="right">32.63</td>
    <td align="right">21.15</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">71.59</td>
    <td align="right">52.93</td>
    <td align="right">40.32</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">31.83</td>
    <td align="right">36.17</td>
    <td align="right">36.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">40.74</td>
    <td align="right">47.38</td>
    <td align="right">25.31</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">92.15</td>
    <td align="right">69.43</td>
    <td align="right">46.44</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">45.16</td>
    <td align="right">48.88</td>
    <td align="right">48.86</td>
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
    <td align="right">47.73</td>
    <td align="right">10.90</td>
    <td align="right">7.87</td>
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
    <td align="right">59.19</td>
    <td align="right">54.71</td>
    <td align="right">41.57</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.10</td>
    <td align="right">19.55</td>
    <td align="right">23.30</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">22.80</td>
    <td align="right">21.55</td>
    <td align="right">24.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">90.23</td>
    <td align="right">82.78</td>
    <td align="right">44.05</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.16</td>
    <td align="right">21.28</td>
    <td align="right">23.75</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.27</td>
    <td align="right">22.38</td>
    <td align="right">24.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">110.38</td>
    <td align="right">101.26</td>
    <td align="right">44.66</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.27</td>
    <td align="right">22.77</td>
    <td align="right">24.28</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">27.52</td>
    <td align="right">24.22</td>
    <td align="right">25.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">140.70</td>
    <td align="right">125.73</td>
    <td align="right">45.26</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">26.87</td>
    <td align="right">24.40</td>
    <td align="right">25.34</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">29.71</td>
    <td align="right">25.55</td>
    <td align="right">26.29</td>
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
    <td align="right">22.89</td>
    <td align="right">41.36</td>
    <td align="right">41.32</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">29.45</td>
    <td align="right">41.63</td>
    <td align="right">41.23</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.62</td>
    <td align="right">25.39</td>
    <td align="right">25.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">27.76</td>
    <td align="right">56.28</td>
    <td align="right">56.90</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.67</td>
    <td align="right">57.79</td>
    <td align="right">57.86</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.60</td>
    <td align="right">36.12</td>
    <td align="right">25.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.45</td>
    <td align="right">76.85</td>
    <td align="right">76.77</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.24</td>
    <td align="right">77.82</td>
    <td align="right">77.72</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.09</td>
    <td align="right">54.87</td>
    <td align="right">39.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">43.92</td>
    <td align="right">86.48</td>
    <td align="right">86.14</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">49.88</td>
    <td align="right">92.39</td>
    <td align="right">92.65</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.10</td>
    <td align="right">55.56</td>
    <td align="right">39.70</td>
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
    <td align="right">18.55</td>
    <td align="right">25.89</td>
    <td align="right">26.23</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.65</td>
    <td align="right">29.00</td>
    <td align="right">28.93</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.81</td>
    <td align="right">31.55</td>
    <td align="right">30.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">18.81</td>
    <td align="right">46.19</td>
    <td align="right">34.93</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.49</td>
    <td align="right">39.88</td>
    <td align="right">27.70</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">20.89</td>
    <td align="right">51.69</td>
    <td align="right">40.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.70</td>
    <td align="right">54.24</td>
    <td align="right">38.25</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">32.84</td>
    <td align="right">53.01</td>
    <td align="right">34.90</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.01</td>
    <td align="right">60.79</td>
    <td align="right">43.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.71</td>
    <td align="right">55.46</td>
    <td align="right">39.04</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.84</td>
    <td align="right">64.35</td>
    <td align="right">44.57</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.51</td>
    <td align="right">64.39</td>
    <td align="right">44.78</td>
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
    <td align="right">25.09</td>
    <td align="right">42.73</td>
    <td align="right">35.08</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.38</td>
    <td align="right">53.58</td>
    <td align="right">40.20</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">36.64</td>
    <td align="right">59.69</td>
    <td align="right">59.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">35.42</td>
    <td align="right">60.27</td>
    <td align="right">35.29</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">41.11</td>
    <td align="right">61.31</td>
    <td align="right">38.13</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">45.39</td>
    <td align="right">77.31</td>
    <td align="right">77.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">40.85</td>
    <td align="right">74.10</td>
    <td align="right">35.91</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.65</td>
    <td align="right">79.29</td>
    <td align="right">39.90</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">47.88</td>
    <td align="right">83.45</td>
    <td align="right">83.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">52.64</td>
    <td align="right">93.71</td>
    <td align="right">37.42</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">57.12</td>
    <td align="right">94.59</td>
    <td align="right">39.69</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">67.32</td>
    <td align="right">118.81</td>
    <td align="right">119.21</td>
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
    <td align="right">65.93</td>
    <td align="right">35.83</td>
    <td align="right">11.91</td>
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
    <td align="right">67.44</td>
    <td align="right">59.76</td>
    <td align="right">46.35</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">22.93</td>
    <td align="right">21.08</td>
    <td align="right">25.95</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">26.09</td>
    <td align="right">22.12</td>
    <td align="right">26.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">99.66</td>
    <td align="right">86.49</td>
    <td align="right">47.66</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">26.14</td>
    <td align="right">27.65</td>
    <td align="right">24.87</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">34.63</td>
    <td align="right">23.17</td>
    <td align="right">25.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">154.11</td>
    <td align="right">193.51</td>
    <td align="right">52.94</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">36.50</td>
    <td align="right">31.61</td>
    <td align="right">28.92</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">35.48</td>
    <td align="right">29.97</td>
    <td align="right">28.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">181.80</td>
    <td align="right">183.51</td>
    <td align="right">58.94</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">41.76</td>
    <td align="right">29.69</td>
    <td align="right">31.21</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">36.77</td>
    <td align="right">30.64</td>
    <td align="right">30.57</td>
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
    <td align="right">25.53</td>
    <td align="right">42.11</td>
    <td align="right">42.01</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.56</td>
    <td align="right">42.99</td>
    <td align="right">42.47</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.03</td>
    <td align="right">30.43</td>
    <td align="right">30.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">31.78</td>
    <td align="right">59.20</td>
    <td align="right">59.17</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">39.72</td>
    <td align="right">62.81</td>
    <td align="right">63.17</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">19.28</td>
    <td align="right">43.21</td>
    <td align="right">31.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">50.58</td>
    <td align="right">95.84</td>
    <td align="right">83.57</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">50.78</td>
    <td align="right">84.22</td>
    <td align="right">85.94</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">36.64</td>
    <td align="right">74.33</td>
    <td align="right">63.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">61.64</td>
    <td align="right">105.07</td>
    <td align="right">110.59</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">76.05</td>
    <td align="right">107.13</td>
    <td align="right">120.50</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">87.07</td>
    <td align="right">134.07</td>
    <td align="right">109.08</td>
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
    <td align="right">20.84</td>
    <td align="right">34.29</td>
    <td align="right">33.02</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">23.67</td>
    <td align="right">36.49</td>
    <td align="right">35.70</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">26.71</td>
    <td align="right">41.27</td>
    <td align="right">54.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">27.11</td>
    <td align="right">64.87</td>
    <td align="right">48.63</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">26.77</td>
    <td align="right">61.02</td>
    <td align="right">34.78</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">25.66</td>
    <td align="right">58.95</td>
    <td align="right">49.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">63.04</td>
    <td align="right">97.79</td>
    <td align="right">65.09</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">46.77</td>
    <td align="right">74.64</td>
    <td align="right">48.55</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">39.32</td>
    <td align="right">71.24</td>
    <td align="right">52.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">52.82</td>
    <td align="right">103.68</td>
    <td align="right">87.94</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">87.13</td>
    <td align="right">167.78</td>
    <td align="right">129.55</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">103.51</td>
    <td align="right">149.16</td>
    <td align="right">132.32</td>
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
    <td align="right">76.39</td>
    <td align="right">92.32</td>
    <td align="right">68.97</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">100.77</td>
    <td align="right">114.83</td>
    <td align="right">87.84</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">42.57</td>
    <td align="right">65.08</td>
    <td align="right">64.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">106.46</td>
    <td align="right">122.22</td>
    <td align="right">76.76</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">131.10</td>
    <td align="right">141.25</td>
    <td align="right">87.19</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">67.46</td>
    <td align="right">107.74</td>
    <td align="right">102.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">132.48</td>
    <td align="right">149.02</td>
    <td align="right">82.89</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">153.25</td>
    <td align="right">172.91</td>
    <td align="right">95.49</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">107.60</td>
    <td align="right">133.29</td>
    <td align="right">120.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">130.07</td>
    <td align="right">157.75</td>
    <td align="right">75.93</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">144.75</td>
    <td align="right">171.81</td>
    <td align="right">87.06</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">118.77</td>
    <td align="right">164.65</td>
    <td align="right">164.02</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
